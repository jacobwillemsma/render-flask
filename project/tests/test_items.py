import os
import unittest

from project import app, db

TEST_DB = 'test.db'


class ProjectTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.create_all()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # tests
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Item Link', response.data)
        self.assertIn(b'Add item', response.data)

    def test_main_page_query_results(self):
        response = self.app.get('/add', follow_redirects=True)
        self.assertIn(b'Add a New Item', response.data)

    def test_add_item(self):
        response = self.app.post(
            '/add',
            data=dict(item_title='Item',
                      item_description='Description',
                      item_comment='Comment'),
            follow_redirects=True)
        self.assertIn(b'New item, Item, added!', response.data)

    def test_add_invalid_item(self):
        response = self.app.post(
            '/add',
            data=dict(item_title='',
                      item_description='test',
                      item_comment='test'),
            follow_redirects=True)
        self.assertIn(b'ERROR! Item was not added.', response.data)
        self.assertIn(b'This field is required.', response.data)


if __name__ == "__main__":
    unittest.main()
