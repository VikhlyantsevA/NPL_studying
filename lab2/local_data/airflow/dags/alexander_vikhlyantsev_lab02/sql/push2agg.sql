INSERT INTO alexander_vikhlyantsev_lab02_agg_hourly (revenue, visitors, buyers, purchases, aov, ts_start, ts_end)
SELECT
    sumIf(item_price, eventType = 'itemBuyEvent') as revenue,
    count(DISTINCT partyId) as visitors,
    count(DISTINCT if(eventType = 'itemBuyEvent', partyId, Null)) as buyers,
    count(DISTINCT if(eventType = 'itemBuyEvent', sessionId, Null)) as purchases,
    if(revenue != 0, revenue / purchases, 0) as aov,
    toStartOfHour(timestamp) as ts_start,
    dateAdd(hour, 1, ts_start) as ts_end
FROM alexander_vikhlyantsev_lab02_rt
WHERE timestamp < (SELECT toStartOfHour(MAX(timestamp)) FROM alexander_vikhlyantsev_lab02_rt) AND
    detectedDuplicate = FALSE AND
    detectedCorruption = FALSE
GROUP BY ts_start;