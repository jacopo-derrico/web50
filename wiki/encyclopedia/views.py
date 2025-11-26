from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title)
    })

def search(request):
    query = request.GET.get('q').lower()
    all_entries = util.list_entries()
    matching_entries = []

    for r in all_entries:
        if r.lower() == query:
            return redirect('entry', title=r)
        elif query in r.lower():
            matching_entries.append(r)

    return render(request, "encyclopedia/search.html", {
            "results": matching_entries,
            "query" : query
    })
        