# Factor taxonomy

Controlled vocabulary for `success_factors` and `failure_factors` in enrichment records. Pick the codes that the sources support; use `other` plus a note in `outcome_analysis` only when none fit. Unknown codes produce a merge warning.

## failure_factors

- `no_market_need`: customers did not have the problem badly enough
- `weak_willingness_to_pay`: interest but no budget
- `market_too_small`: real need but too few customers for a venture outcome
- `market_timing_early`: market or technology was not ready
- `market_timing_late`: market already taken or moved on
- `ran_out_of_money`: burned cash without reaching the next milestone
- `could_not_raise_next_round`: traction was real but insufficient for the next round
- `competition_won`: a competitor out-executed it
- `incumbent_copied`: a larger player shipped a substitute or absorbed the wedge
- `platform_dependency`: relied on a platform that changed terms or access
- `regulatory_blocked`: regulation or licensing blocked or killed the model
- `unit_economics`: each customer lost money or growth required unaffordable spend
- `distribution_failed`: could not reach customers cost-effectively
- `tech_unsolved`: the core technical problem was not solved
- `scaling_failed`: worked at small scale, broke when scaled
- `founder_conflict`: founders split or fell out
- `pivot_failed`: pivoted without finding a better position
- `acquihire_soft_landing`: team absorbed by an acquirer without a real product outcome
- `fraud_or_legal`: fraud, litigation or legal exposure
- `macro_downturn`: funding or demand environment collapsed
- `other`: none of the above (explain in outcome_analysis)

## success_factors

- `strong_pmf`: clear, measurable product-market fit
- `large_market_growth`: market grew fast
- `timing_tailwind`: technology, regulation or behavior shift helped
- `distribution_advantage`: unusually efficient or owned distribution
- `network_effects`: value grew with users
- `technical_moat`: hard-to-replicate technology
- `regulatory_moat`: licenses or compliance position others lacked
- `switching_costs`: deep integration or data lock-in
- `proprietary_data`: compounding or exclusive data
- `founder_market_fit`: founders had unusual domain insight or access
- `strong_team_execution`: exceptional speed and hiring
- `capital_efficiency`: reached milestones cheaply
- `successful_pivot`: a pivot found the real market
- `incumbent_weakness`: incumbents were slow, hated or unable to respond
- `product_led_growth`: product spread through use
- `enterprise_sales_engine`: repeatable high-value sales motion
- `other`: none of the above (explain in outcome_analysis)
