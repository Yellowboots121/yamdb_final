from collections import OrderedDict
import csv

from django.apps import apps
from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Comment, Category, Genre, Title, TitleGenre, Review
from users.models import User


MODELS_FIELDS = {
    'category': Category,
    'genre': Genre,
    'title': Title,
    'author': User,
    'review': Review,
}

DEFAULT_DATASET = OrderedDict({
    'users.csv': User,
    'genre.csv': Genre,
    'category.csv': Category,
    'titles.csv': Title,
    'genre_title.csv': TitleGenre,
    'review.csv': Review,
    'comments.csv': Comment,
})

DEFAULT_DATASET_PATH = 'static/data/'


class Command(BaseCommand):
    help = 'Creating model objects according the file path specified'

    @staticmethod
    def dict_reader_csv(csv_file, model):
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            for field, value in row.items():
                if field in MODELS_FIELDS.keys():
                    row[field] = get_object_or_404(
                        MODELS_FIELDS[field], pk=value
                    )
            model.objects.create(**row)

    def add_arguments(self, parser):
        parser.add_argument(
            '--use_default_dataset',
            action='store_true',
            help="use it to default dataset upload"
        )

        parser.add_argument('--path', type=str, help="file path")
        parser.add_argument('--model_name', type=str, help="model name")
        parser.add_argument(
            '--app_name',
            type=str,
            help="django app name that the model is connected to"
        )

    def handle(self, *args, **options):
        if options['use_default_dataset']:
            for filename, model in DEFAULT_DATASET.items():
                with open(
                        DEFAULT_DATASET_PATH + filename, 'rt', encoding='utf-8'
                ) as csv_file:
                    self.dict_reader_csv(csv_file, model)
        else:
            file_path = options['path']
            model = apps.get_model(options['app_name'], options['model_name'])
            with open(file_path, 'rt', encoding='utf-8') as csv_file:
                self.dict_reader_csv(csv_file, model)
