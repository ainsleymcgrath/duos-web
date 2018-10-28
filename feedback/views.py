# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


from feedback.db.query import Query


def index(request):
    context = {"title": "Collecting feedback from DUOS' subjects"}
    return render(request, "feedback/index.html", context)


@require_http_methods(["GET", "POST"])
def author_survey(request, author_id, article_id):

    # handle form submission
    if request.method == "POST":
        return HttpResponse("nice")

    q = Query()
    # every reference to a dataset in this article
    references = q.survey(author_id, article_id)

    # distinct datasets (dupes b/c of above granularity)
    dataset_names = list({ref["datasetname"] for ref in references})

    props = {
        "authorName": q.author_name(author_id),
        "authorId": author_id,
        "articleName": q.article_name(article_id),
        "articleId": article_id,
        "datasets": [{"name": name} for name in dataset_names],  # TODO: need an ID
    }

    context = {"props": json.dumps(props)}
    q.close()
    return render(request, "feedback/author_survey.html", context)

