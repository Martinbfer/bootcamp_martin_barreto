# Stage 14: Deployment & Monitoring – Reflection

Deploying the KO 5-year return prediction model introduces several credible risks.  
The most important **failure modes** include: (1) **schema drift**, where upstream data changes break the feature pipeline;  
(2) **increased null values**, which reduce input quality; (3) **label delay**, since realized returns are only known in the future;  
(4) **concept drift**, when market regimes shift and past relationships no longer hold; and (5) **system outages** affecting the API.

For each risk, a **monitoring metric and threshold** is required: schema drift → monitor schema hash daily (alert if mismatch);  
null values → track missing rate (alert if >2%); label delay → monitor lag between prediction and outcome (alert if >7 days);  
concept drift → monitor Population Stability Index on key features (alert if PSI >5%); system outages → monitor uptime and latency  
(p95 latency must stay <300ms, job success >99%).

**Alert recipients and runbook steps**: Data issues are routed to the **data engineering on-call**, first step: check ingestion logs.  
Model drift or degraded accuracy is routed to the **ML engineering team**, first step: validate feature distributions and compare to baseline.  
System outages go to the **platform team**, first step: restart failing service. Business KPI drops trigger a review by the **business analyst**,  
first step: confirm if the decline is model-driven or external.

**Retraining cadence/triggers**: model retrains quarterly or sooner if PSI >5% on key features or if rolling 2-week accuracy falls 10% below baseline.

**Ownership**: Data engineers maintain data dashboards, ML engineers maintain model dashboards and approve retrains, platform engineers approve  
rollbacks, and analysts review business KPIs weekly. All issues are logged in the shared project tracker for transparency.

This layered monitoring ensures risks are visible, responsibilities are clear, and actions are defined.

