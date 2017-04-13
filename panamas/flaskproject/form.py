#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is used to create a from for our Flask application"""

from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required, Email, DataRequired, Length, InputRequired,EqualTo
from neo4j.v1 import GraphDatabase, basic_auth

""" Class SignupForm : class test to test the module flask_wtf
    :param FlaskForm: class form of WTForms
"""
class SignupForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(),
                                           Length(max=20, message=(u'Please give a name shorter'))])
 

    submit = SubmitField(u'Signup')


""" Class TestForm notre classe pour le formulaire que l'on proposera
    à l'utilisateur
    :param FlaskForm: class form of WTForms
"""
class TestForm(FlaskForm):
    """
        Notre formulaire demande un nom, un label de départ pour un noeud,
        un autre label pour le noeud d'arrivée
    """
    name = StringField('Name or part of name',
                       validators=[DataRequired("Write something please"),
                                   Length(min=1, message=("Please give a longer name "))])
    label_d = SelectField(u'Label de départ',
                          choices=[('Intermediary','Intermediary'),
                                       ('Address','Address'),
                                       ('Officer','Officer'),
                                       ('Entity','Entity'),
                                       ('Country','Country')],
                          validators=[InputRequired("You need to select a label")])
    label_f = SelectField(u'Label d\'arrivée',
                          choices=[('Intermediary','Intermediary'),
                                       ('Address','Address'),
                                       ('Officer','Officer'),
                                       ('Entity','Entity'),
                                       ('Country','Country')],
                          validators=[InputRequired("You need to select a label")])


class CountryForm(FlaskForm):
    choices=[()]

    country1 = SelectField(u'Country départ',choices=choices)
    country2 = SelectField(u'Country arrivée',choices=choices)
