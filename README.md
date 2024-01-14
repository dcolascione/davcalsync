Basic EWS-to-CalDAV one-way sync program

We try to work around idiosyncrasies in Google's implementation of
CalDAV: if updating a recurring event fails with a mysterious "409
Conflict" message, we try "deleting" the event and trying again.
That usually works.
