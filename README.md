# UGE2-MANDAG---Requests-BeautifulSoup-statisk-HTML-

### Hvorfor statiske sider:

Python modulet "requests" henter kun html filen,
Og den kører ikke noget kode der er indbygget på hjemmesiden.

Hvis requests prøver at hente en dynamisk side vil den hente tomme div containere uden data.

### Hvilke HTML-elementer vælger man og hvorfor?

    

Jeg har lært at hjemmesider har beskyttelse mod hurtige forespørgsler.
Der for skal man tilføje en debounce i koden.