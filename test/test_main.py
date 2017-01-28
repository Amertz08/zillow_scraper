from __future__ import absolute_import, print_function, unicode_literals

from test import BaseTest
from app.models import HomeListing
from app.lib import commit


class TestMain(BaseTest):

    def test_index(self):
        r = self.client.get('/')
        self.assert200(r, 'Index view does not return 200')
        self.assertTemplateUsed('index.html')

    def test_listings_none(self):
        r = self.client.get('/listings')
        self.assert200(r, 'Listings view does not return 200')
        self.assertTemplateUsed('listings.html')
        listings = self.get_context_variable('listings')
        self.assertEqual(listings, [], 'Listings context: {}'.format(listings))

    def test_one_listing(self):
        listing = HomeListing(
            zid=123
        )
        self.db.session.add(listing)
        commit(self.db.session)
        r = self.client.get('/listings')
        self.assert200(r, 'Listing view does not return 200')
        listing = HomeListing.query.first()
        context_var = self.get_context_variable('listings')
        self.assertEqual(len(context_var), 1, 'There should only be on listing: {}'.format(len(context_var)))
        self.assertEqual(context_var.pop(), listing, 'blah')
