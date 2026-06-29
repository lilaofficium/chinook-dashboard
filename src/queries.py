INVOICES_QUERY = """
    SELECT i.invoice_id,
           i.customer_id,
           i.invoice_date,
           i.billing_country,
           i.total
    FROM   public.invoice i
"""

INVOICE_LINE_DETAIL_QUERY = """
    SELECT il.invoice_id,
           ar.name                          AS artist,
           il.unit_price * il.quantity      AS line_total
    FROM   public.invoice_line il
    JOIN   public.track  t  ON il.track_id  = t.track_id
    JOIN   public.album  al ON t.album_id   = al.album_id
    JOIN   public.artist ar ON al.artist_id  = ar.artist_id
"""