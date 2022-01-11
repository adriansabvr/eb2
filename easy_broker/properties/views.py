from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .easy_broker import EasyBrokerClient, Status, EasyBrokerClientError
from .forms import ContactForm
from django.urls import reverse
from django.http import Http404

api_key = "l7u502p8v46ba3ppgvj5y2aad50lb9"


def PropertyDetailView(request, property_id):
    eb_client = EasyBrokerClient(api_key)

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            payload = {
                "name": form.cleaned_data["name"],
                "phone": form.cleaned_data["phone"],
                "message": form.cleaned_data["message"],
                "email": form.cleaned_data["email"],
                "property_id": property_id,
                "source": "Real Estate Agency",
            }
            response = eb_client.post_contact_request(payload)
            if isinstance(response, EasyBrokerClientError):
                raise Http404(response.error_msg)
            return HttpResponseRedirect(
                reverse("properties:property", kwargs={"property_id": property_id}) + "?okcreated"
            )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
        response = eb_client.get_property(property_id)
        if isinstance(response, EasyBrokerClientError):
            raise Http404(response.error_msg)
        return render(request, "property_detail.html", {"property": response, "form": form})


def PropertyListView(request):
    paginate_by = 15
    page = request.GET.get("page")
    page_number = 1 if page is None else int(page)
    eb_client = EasyBrokerClient(api_key)

    # Published properties
    response = eb_client.get_properties(page_number, paginate_by, {}, [Status.PUBLISHED])

    if isinstance(response, EasyBrokerClientError):
        raise Http404(response.error_msg)

    pagination = response["pagination"]
    has_next = pagination["next_page"] != None
    has_previous = page_number > 1

    page_obj = {
        "has_previous": has_previous,
        "has_next": has_next,
        "previous_page": page_number - 1,
        "next_page": page_number + 1,
    }

    properties = response["content"]
    if len(properties) == 0:
        raise Http404("Page not Found")

    return render(request, "property_list.html", {"properties": properties, "page_obj": page_obj})
