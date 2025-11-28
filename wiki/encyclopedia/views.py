from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

import random

from . import util
from markdown2 import Markdown

# generic function to convert .md to html
def toHTML(file):
    markdowner = Markdown(extras=[""])
    return markdowner.convert(file)

# new entry form
class NewEntryForm(forms.Form):
    new_title = forms.CharField(label="Enter title", max_length=50)
    new_markdown = forms.CharField(label="Enter the markdown of the wiki", widget=forms.Textarea)

# edit entry form
class EditEntryForm(forms.Form):
    edit_markdown = forms.CharField(label="Edit the markdown of the wiki here", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def error(request):
    return render(request, "encyclopedia/404.html")

def entry(request, title):
    entry = util.get_entry(title)

    if entry == None:
        return redirect('error')
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "text": toHTML(entry)
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

def new(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        all_entries = util.list_entries()

        if form.is_valid():
            title = form.cleaned_data["new_title"]
            markdown = form.cleaned_data["new_markdown"]

            for r in all_entries:
                if r.lower() == title:
                    error = "Entry title already existing"
                    return render(request, "encyclopedia/new.html", {
                        "form": form,
                        "error": error
                    })
            
            util.save_entry(title, markdown)

            new_entry = util.get_entry(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "text": toHTML(new_entry)                
            })
    else:
        return render(request, "encyclopedia/new.html", {
            "form": NewEntryForm
        })
    
def edit(request, title):
    if request.method == 'POST':
        form = EditEntryForm(request.POST)

        if form.is_valid():
            markdown = form.cleaned_data["edit_markdown"]

            util.save_entry(title, markdown)

            entry = util.get_entry(title)

            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "text": toHTML(entry)                
            })
    else:
        entry = util.get_entry(title)
        form = EditEntryForm(initial={
            'edit_markdown': entry
        })

        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "form": form
        })
        
def random_page(request):
    all_entries = util.list_entries()

    random_entry = random.choice(all_entries)

    # entry = util.get_entry(random_entry)

    return redirect('entry', title=random_entry)