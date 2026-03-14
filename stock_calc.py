#!/usr/bin/env python

def calculate_dividend_growth_rate(d, pb, pe):
    """
    计算：股息率 + 净利润增长率

    Args:
        dividend_rate: 分红率 (0-1)
        pb: 市净率
        pe: 市盈率

    Returns:
        (总和, 股息率, 净利润增长率)
    """
    total = (d + (1 - d) * pb) / pe
    dividend_yield = d / pe
    net_profit_growth = (1 - d) * pb / pe

    return (
        total,
        dividend_yield,
        net_profit_growth,
    )


if __name__ == "__main__":
    dividend_rate = eval(input("分红率%: ")) / 100
    pb = eval(input("市净率 PB: "))
    pe = eval(input("市盈率 PE: "))

    total, dividend_yield, net_profit_growth = calculate_dividend_growth_rate(
        dividend_rate, pb, pe
    )

    print("\n" + "=" * 50)
    print("计算结果:")
    print("=" * 50)
    print(f"  股息率:       {dividend_yield * 100:6.2f}%")
    print(f"  净利润增长率: {net_profit_growth * 100:6.2f}%")
    print("-" * 50)
    print(f"  总和:         {total * 100:6.2f}%")
    print("=" * 50)

