import streamlit as st
import dash_bootstrap_components as dbc
from dash import html


def __header_Card():

    dbc.Card(
        [
            dbc.CardImg(src="https://getbootstrap.com/static/images/placeholder286x180.png", top=True),
            dbc.CardBody(
                [
                    html.H4("Card title", className="card-title"),
                    html.P(
                        "Some quick example text to build on the card title and "
                        "make up the bulk of the card's content.",
                        className="card-text",
                    ),
                    dbc.Button("Go somewhere", color="primary"),
                ]
            ),
        ],
        style={"width": "18rem"},
    )


__header_Card()