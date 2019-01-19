from django.shortcuts import render, redirect
from .models import PortData
import csv
from django.contrib import messages
from io import TextIOWrapper
from rest_framework import viewsets
from .serializers import DataSerializer


def index(request):
    return render(request, 'portdata/index.html')


def upload(request):
    try:
        files = request.FILES.getlist('uploadfiles')
        for f in files:
            file_reader = csv.reader(TextIOWrapper(f), delimiter=',')
            next(file_reader, None)
            try:
                for row in file_reader:
                    obj, created = PortData.objects.get_or_create(
                        product=row[0],
                        quantity=row[1],
                        unit=row[2],
                        item_rate_inv=row[3],
                        currency=row[4],
                        total_amount=row[5],
                        fob_inr=row[6],
                        item_rate_inr=row[7],
                        fob_usd=row[8],
                        foreign_port=row[9],
                        foreign_country=row[10],
                        india_port=row[11],
                        india_company=row[12],
                        foreign_company=row[13],
                        invoice_number=row[14],
                        hs_code=row[15],
                    )
            except:
                messages.add_message(request, messages.ERROR, 'Error importing file ' + f.name + '. Skipping this.')
        messages.add_message(request, messages.SUCCESS, 'Data imported.')
    except:
        messages.add_message(request, messages.ERROR, 'Error importing data.')
    return redirect('index')


class DataViewSet(viewsets.ModelViewSet):
    queryset = PortData.objects.all()
    serializer_class = DataSerializer
