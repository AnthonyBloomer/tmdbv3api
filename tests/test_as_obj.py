import sys
from unittest import TestCase
from tmdbv3api.as_obj import AsObj


class AsObjTests(TestCase):
    def setUp(self):
        self.entries = {
            'title': 'images',
            'results': [
                {
                    'path': 'img/',
                    'title': 'img1'
                },
                {
                    'path': 'img/',
                    'title': 'img2'
                }
            ],
            'formats': ['.jpg', '.png'],
            'languages': {
                'ES': 'es-ES',
                'FR': 'fr-FR'
            }
        }

    def assert_attr(self, dict_obj):
        self.assertIsNotNone(dict_obj)

        self.assertTrue(hasattr(dict_obj, 'title'))
        self.assertTrue(isinstance(dict_obj.title, str))
        self.assertEqual(dict_obj.title, 'images')

        self.assertTrue(hasattr(dict_obj, 'results'))
        self.assertTrue(isinstance(dict_obj.results, AsObj))
        self.assertTrue(dict_obj.results._list_only)
        for result in dict_obj.results:
            self.assertTrue(isinstance(result, AsObj))
            self.assertTrue(hasattr(result, 'path'))
            self.assertTrue(hasattr(result, 'title'))
            self.assertTrue(isinstance(result.path, str))
            self.assertTrue(isinstance(result.title, str))

        self.assertTrue(hasattr(dict_obj, 'formats'))
        self.assertTrue(isinstance(dict_obj.formats, AsObj))
        self.assertTrue(dict_obj.formats._list_only)
        self.assertIn('.jpg', dict_obj.formats)
        self.assertIn('.png', dict_obj.formats)

        self.assertTrue(hasattr(dict_obj, 'languages'))
        self.assertTrue(isinstance(dict_obj.languages, AsObj))
        self.assertTrue(hasattr(dict_obj.languages, 'ES'))
        self.assertTrue(hasattr(dict_obj.languages, 'FR'))
        self.assertTrue(isinstance(dict_obj.languages.ES, str))
        self.assertTrue(isinstance(dict_obj.languages.FR, str))
        self.assertEqual(dict_obj.languages.ES, 'es-ES')
        self.assertEqual(dict_obj.languages.FR, 'fr-FR')

    def assert_dict(self, dict_obj):
        self.assertIsNotNone(dict_obj)

        self.assertIn('title', dict_obj)
        self.assertTrue(isinstance(dict_obj['title'], str))
        self.assertEqual(dict_obj['title'], 'images')

        self.assertIn('results', dict_obj)
        self.assertTrue(isinstance(dict_obj['results'], AsObj))
        self.assertTrue(dict_obj['results']._list_only)
        for result in dict_obj['results']:
            self.assertTrue(isinstance(result, AsObj))
            self.assertIn('path', result)
            self.assertIn('title', result)
            self.assertTrue(isinstance(result['path'], str))
            self.assertTrue(isinstance(result['title'], str))

        self.assertIn('formats', dict_obj)
        self.assertTrue(isinstance(dict_obj['formats'], AsObj))
        self.assertTrue(dict_obj['formats']._list_only)
        self.assertIn('.jpg', dict_obj['formats'])
        self.assertIn('.png', dict_obj['formats'])

        self.assertIn('languages', dict_obj)
        self.assertTrue(isinstance(dict_obj['languages'], AsObj))
        self.assertIn('ES', dict_obj['languages'])
        self.assertIn('FR', dict_obj['languages'])
        self.assertTrue(isinstance(dict_obj['languages']['ES'], str))
        self.assertTrue(isinstance(dict_obj['languages']['FR'], str))
        self.assertEqual(dict_obj['languages']['ES'], 'es-ES')
        self.assertEqual(dict_obj['languages']['FR'], 'fr-FR')

    def test_dict_obj__init__(self):
        dict_obj = AsObj(self.entries)
        self.assert_attr(dict_obj)
        self.assert_dict(dict_obj)
        self.assert_dict(dict_obj.__dict__)

    def test_dict_obj__len__(self):
        self.assertEqual(len(AsObj({'a': 1, 'b': 2})), 2)
        self.assertEqual(len(AsObj()), 0)

    def test_dict_obj__getitem__(self):
        dict_obj = AsObj(self.entries)
        self.assertEqual(dict_obj['title'], 'images')
        self.assertEqual(dict_obj['results'][0]['path'], 'img/')
        self.assertEqual(dict_obj['formats'][0], '.jpg')
        self.assertEqual(dict_obj['languages']['ES'], 'es-ES')

    def test_dict_obj__setitem__(self):
        dict_obj = AsObj()
        dict_obj['title'] = 'images'
        dict_obj['results'] = [{'path': 'img/'}]
        dict_obj['formats'] = ['.jpg']
        dict_obj['languages'] = {'ES': 'es-ES'}
        self.assertEqual(dict_obj['title'], 'images')
        self.assertEqual(dict_obj['results'][0]['path'], 'img/')
        self.assertEqual(dict_obj['formats'][0], '.jpg')
        self.assertEqual(dict_obj['languages']['ES'], 'es-ES')

    def test_dict_obj__delitem__(self):
        dict_obj = AsObj(self.entries)
        self.assertIn('title', dict_obj)
        del dict_obj['title']
        self.assertNotIn('title', dict_obj)

    def test_dict_obj__iter__(self):
        try:
            iter(AsObj(self.entries))
        except TypeError:
            self.fail('Not iterable')

    def test_dict_obj__reversed__(self):
        if sys.version_info >= (3, 8):
            try:
                reversed(AsObj(self.entries))
            except TypeError:
                self.fail('Not reverse iterable')

    def test_dict_obj_copy(self):
        dict_obj = AsObj(self.entries)
        dict_obj_copy = dict_obj.copy()
        self.assertTrue(hasattr(dict_obj_copy, 'title'))

    def test_dict_obj_get(self):
        get = AsObj(self.entries).get('title')
        self.assertEqual(get, 'images')

    def test_dict_obj_items(self):
        items = AsObj(self.entries).items()
        self.assertEqual(len(items), 4)
        self.assertIn(('title', 'images'), items)

    def test_dict_obj_keys(self):
        keys = AsObj(self.entries).keys()
        self.assertEqual(len(keys), 4)
        self.assertIn('title', keys)

    def test_dict_obj_pop(self):
        dict_obj = AsObj(self.entries)
        pop = dict_obj.pop('title')
        self.assertNotIn('title', dict_obj)
        self.assertEqual(pop, 'images')
        pop = dict_obj.pop('random', 'not_exists')
        self.assertEqual(pop, 'not_exists')

    def test_dict_obj_popitem(self):
        popitem = AsObj(self.entries).popitem()
        self.assertIsNotNone(popitem)

    def test_dict_obj_setdefault(self):
        dict_obj = AsObj(self.entries)
        self.assertEqual(dict_obj.setdefault('title'), 'images')
        self.assertEqual(dict_obj.setdefault('random', 'modern'), 'modern')

    def test_dict_obj_update(self):
        dict_obj = AsObj()
        dict_obj.update(self.entries)
        self.assertTrue(hasattr(dict_obj, 'title'))

    def test_dict_obj_values(self):
        values = AsObj(self.entries).values()
        self.assertEqual(len(values), 4)
        self.assertIn('images', values)
