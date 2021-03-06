from email.utils import parsedate
from datetime import datetime
import time

class Email:
    def __init__(self, messageid, fromEmail, fromName, inreplyto,
    date, subject, content, listnames, references):
        self.message_id = messageid
        self.from_email = fromEmail
        self.from_name = fromName
        self.date = date
        self.in_reply_to = inreplyto
        self.subject = info = (subject[:298] + '..') if len(subject) > 300 else subject
        self.content = content
        self.list_names = listnames
        self.references = list(set(references))

    def __str__(self):
        return "<%s> - From: %s (%s) \n \
        List: %s - subject: %s, date: %s" % (self.messageid, self.fromName,
        self.fromEmail, self.listnames, self.subject, self.dateString)
