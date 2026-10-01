# Olist E-commerce Analytics (SQL + Python + Streamlit)

**Live dashboard:** [add link after deployment]

## Business question
Where is the business losing revenue and customers, and what should it do about it?

## Data and method
Olist Brazilian e-commerce dataset: 9 related tables, ~100k orders. I loaded it into SQLite and did the analysis with multi-table JOINs, CTEs, `CASE WHEN`, and window functions (`LAG`, `SUM() OVER`). Python was used for cohorts and charts.

- Scope: delivered orders, Jan 2017 - Aug 2018 (the first and last months of the data are partial, so excluded).
- Used `customer_unique_id`, not `customer_id`, to identify real customers (`customer_id` changes with every order).

## Key findings
1. **Revenue plateaued after Black Friday 2017.** Nov 2017 hit 987,765, and every 2018 month stayed between 826k and 978k. Orders drifted from 7,069 (Jan) to 6,351 (Aug) while average order value held at 126-145, so the stall is about volume, not basket size.
2. **97% of customers buy only once** (90,315 of 93,104). Repeat customers are 3.0% of customers and 5.5% of revenue.
3. **Retention is very low:** average month-1 cohort retention is 0.48%, and it stays flat in later months rather than building.
4. **Late deliveries hurt reviews.** 8.0% of orders arrive late and average 2.57 stars vs. 4.30 for on-time. Reviews collapse past 3 days late (61% 1-2 star at 4-7 days late, 78% at 8+).
5. **A late first order is associated with fewer repeat purchases:** 3.10% vs. 4.05%.
6. **Late rates vary by state:** MA 19.6%, CE 15.4%, BA 14.0%, RJ 13.5% vs. 8.0% overall. RJ is not the worst rate, but its volume makes it roughly a fifth of all late orders.

## Recommendations
1. **Build a second-purchase program** (post-delivery email or offer within 30 days), since almost all growth depends on winning new customers.
2. **Fix delivery promises, not just delivery speed:** reviews drop sharply once an order is more than 3 days late, so set realistic estimates or alert customers early in high-late states (RJ for volume, MA and CE for rate).
3. **Test these ideas before scaling:** run an A/B test on the retention offer and on revised delivery estimates.

## Limitations
- Findings on lateness and repeat purchase are associations, not proven causes (state, category, and seller also vary).
- The 20-month window leaves recent customers little time to return.
- Olist is a marketplace, so some low repeat rate is expected.
- Revenue = item price, excluding shipping.

## Files
- `olist_analysis.ipynb`: SQL and Python analysis
- `app.py`: Streamlit dashboard
- CSVs: precomputed results used by the dashboard