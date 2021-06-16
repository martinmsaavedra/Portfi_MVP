#!/usr/bin/python3
'''Polulates Database from Yahoo Query API'''
from models.Asset import Asset
from yahooquery import Ticker
from models.engine.db_storage import DBStorage
from datetime import datetime, time

storage = DBStorage()
storage.reload()
#tickers = ["VCSH", "HYG", "LQD", "AGG", "VCIT", "ANGL", "ACWI", "MOAT", "EFA", "SPY", "SPHQ", "EEM", "XLF", "EMQQ", "VB", "CEF"]
#ABT ABBV ABMD ACN ATVI ADBE AMD AAP AES AFL A APD AKAM ALK ALB ARE ALXN ALGN ALLE ALL AMZN AMCR AEE AAL AEP AXP AIG AMT AWK AMP ABC AME AMGN APH ADI ANSS ANTM AON AOS APA AAPL AMAT APTV ADM ANET AJG AIZ ATO ADSK ADP AZO AVB AVY AVGO BKR BLL BAC BK BAX BDX BRK.B BBY BIO BIIB BLK BA BKNG BWA BXP BSX BMY BR BF.B BEN CHRW COG CDNS CZR CPB COF CAH CCL CARR CTLT CAT CBOE CBRE CDW CE CNC CNP CERN CF CRL CHTR CVX CMG CB CHD CI CINF CTAS CSCO C CFG CTXS CLX CME CMS CTSH CL CMCSA CMA CAG COP COO CPRT CTVA COST CCI CSX CMI CVS CRM DHI DHR DRI DVA DE DAL DVN DXCM DLR DFS DISCA DISCK DISH DG DLTR D DPZ DOV DOW DTE DUK DRE DD DXC DGX DIS ED EMN ETN EBAY ECL EIX EW EA EMR ENPH ETR EOG EFX EQIX EQR ESS EL ETSY EVRG ES EXC EXPE EXPD EXR FANG FFIV FB FAST FRT FDX FIS FITB FE FRC FISV FLT FMC F FTNT FTV FBHS FOXA FOX FCX GOOGL GOOG GLW GPS GRMN GNRC GD GE GIS GM GPC GILD GL GPN GS GWW HAL HBI HIG HAS HCA HSIC HSY HES HPE HLT HFC HOLX HD HON HRL HST HWM HPQ HUM HBAN HII IT IEX IDXX INFO ITW ILMN INCY IR INTC ICE IBM IP IPG IFF INTU ISRG IVZ IPGP IQV IRM JKHY J JBHT JNJ JCI JPM JNPR KMX KO KSU K KEY KEYS KMB KIM KMI KLAC KHC KR LNT LB LHX LH LRCX LW LVS LEG LDOS LEN LLY LNC LIN LYV LKQ LMT L LOW LUMN LYB LUV MMM MO MTB MRO MPC MKTX MAR MMC MLM MAS MA MKC MXIM MCD MCK MDT MRK MET MTD MGM MCHP MU MSFT MAA MHK MDLZ MPWR MNST MCO MS MOS MSI MSCI NDAQ NTAP NFLX NWL NEM NWSA NWS NEE NLSN NKE NI NSC NTRS NOC NLOK NCLH NOV NRG NUE NVDA NVR NXPI NOW ORLY OXY ODFL OMC OKE ORCL OTIS O PEAK PCAR PKG PH PAYX PAYC PYPL PENN PNR PBCT PEP PKI PRGO PFE PM PSX PNW PXD PNC POOL PPG PPL PFG PG PGR PLD PRU PTC PEG PSA PHM PVH PWR QRVO QCOM RE RL RJF RTX REG REGN RF RSG RMD RHI ROK ROL ROP ROST RCL SCHW STZ SJM SPGI SBAC SLB STX SEE SRE SHW SPG SWKS SNA SO SWK SBUX STT STE SYK SIVB SYF SNPS SYY T TAP TMUS TROW TTWO TPR TGT TEL TDY TFX TER TSLA TXN TXT TMO TJX TSCO TT TDG TRV TRMB TFC TWTR TYL TSN UDR ULTA USB UAA UA UNP UAL UNH UPS URI UHS UNM VLO VTR VRSN VRSK VZ VRTX VFC VIAC VTRS V VNO VMC WRB WAB WMT WBA WM WAT WEC WFC WELL WST WDC WU WRK WY WHR WMB WLTW WYNN XRAY XOM XEL XLNX XYL YUM ZBRA ZBH ZION ZTS"
tickers = ["VCSH", "HYG", "LQD" "AGG", "VCIT", "ANGL", "ACWI", "MOAT", "EFA", "SPY", "SPHQ", "EEM", "XLF", "EMQQ", "VB", "CEF", "ABT", "ABBV", "ABMD", "ACN", "ATVI", "ADBE", "AMD", "AAP", "AES", "AFL", "A", "APD", "AKAM", "ALK", "ALB", "ARE", "ALXN", "ALGN", "ALLE", "ALL", "AMZN", "AMCR", "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "ADI", "ANSS", "ANTM", "AON", "AOS", "APA", "AAPL", "AMAT", "APTV", "ADM", "ANET", "AJG", "AIZ", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "AVGO", "BKR", "BLL", "BAC", "BK", "BAX", "BDX", "BBY", "BIO", "BIIB", "BLK", "BA", "BKNG", "BWA", "BXP", "BSX", "BMY", "BR", "BEN", "CHRW", "COG", "CDNS", "CZR", "CPB", "COF", "CAH", "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE", "CDW", "CE", "CNC", "CNP", "CERN", "CF", "CRL", "CHTR", "CVX", "CMG", "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG", "CTXS", "CLX", "CME", "CMS", "CTSH", "CL", "CMCSA", "CMA", "CAG", "COP", "COO", "CPRT", "CTVA", "COST", "CCI", "CSX", "CMI", "CVS", "CRM", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "DVN", "DXCM", "DLR", "DFS", "DISCA", "DISCK", "DISH", "DG", "DLTR", "D", "DPZ", "DOV", "DOW", "DTE", "DUK", "DRE", "DD", "DXC", "DGX", "DIS", "ED", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "EMR", "ENPH", "ETR", "EOG", "EFX", "EQIX", "EQR", "ESS", "EL", "ETSY", "EVRG", "ES", "EXC", "EXPE", "EXPD", "EXR", "FANG", "FFIV", "FB", "FAST", "FRT", "FDX", "FIS", "FITB", "FE", "FRC", "FISV", "FLT", "FMC", "F", "FTNT", "FTV", "FBHS", "FOXA", "FOX", "FCX", "GOOGL", "GOOG", "GLW", "GPS", "GRMN", "GNRC", "GD", "GE", "GIS", "GM", "GPC", "GILD", "GL", "GPN", "GS", "GWW", "HAL", "HBI", "HIG", "HAS", "HCA", "HSIC", "HSY", "HES", "HPE", "HLT", "HFC", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ", "HUM", "HBAN", "HII", "IT", "IEX", "IDXX", "INFO", "ITW", "ILMN", "INCY", "IR", "INTC", "ICE", "IBM", "IP", "IPG", "IFF", "INTU", "ISRG", "IVZ", "IPGP", "IQV", "IRM", "JKHY", "J", "JBHT", "JNJ", "JCI", "JPM", "JNPR", "KMX", "KO", "KSU", "K", "KEY", "KEYS", "KMB", "KIM", "KMI", "KLAC", "KHC", "KR", "LNT", "LB", "LHX", "LH", "LRCX", "LW", "LVS", "LEG", "LDOS", "LEN", "LLY", "LNC", "LIN", "LYV", "LKQ", "LMT", "L", "LOW", "LUMN", "LYB", "LUV", "MMM", "MO", "MTB", "MRO", "MPC", "MKTX", "MAR", "MMC", "MLM", "MAS", "MA", "MKC", "MXIM", "MCD", "MCK", "MDT", "MRK", "MET", "MTD", "MGM", "MCHP", "MU", "MSFT", "MAA", "MHK", "MDLZ", "MPWR", "MNST", "MCO", "MS", "MOS", "MSI", "MSCI", "NDAQ", "NTAP", "NFLX", "NWL", "NEM", "NWSA", "NWS", "NEE", "NLSN", "NKE", "NI", "NSC", "NTRS", "NOC", "NLOK", "NCLH", "NOV", "NRG", "NUE", "NVDA", "NVR", "NXPI", "NOW", "ORLY", "OXY", "ODFL", "OMC", "OKE", "ORCL", "OTIS", "O", "PEAK", "PCAR", "PKG", "PH", "PAYX", "PAYC", "PYPL", "PENN", "PNR", "PBCT", "PEP", "PKI", "PRGO", "PFE", "PM", "PSX", "PNW", "PXD", "PNC", "POOL", "PPG", "PPL", "PFG", "PG", "PGR", "PLD", "PRU", "PTC", "PEG", "PSA", "PHM", "PVH", "PWR", "QRVO", "QCOM", "RE", "RL", "RJF", "RTX", "REG", "REGN", "RF", "RSG", "RMD", "RHI", "ROK", "ROL", "ROP", "ROST", "RCL", "SCHW", "STZ", "SJM", "SPGI", "SBAC", "SLB", "STX", "SEE", "SRE", "SHW", "SPG", "SWKS", "SNA", "SO", "SWK", "SBUX", "STT", "STE", "SYK", "SIVB", "SYF", "SNPS", "SYY", "T", "TAP", "TMUS", "TROW", "TTWO", "TPR", "TGT", "TEL", "TDY", "TFX", "TER", "TSLA", "TXN", "TXT", "TMO", "TJX", "TSCO", "TT", "TDG", "TRV", "TRMB", "TFC", "TWTR", "TYL", "TSN", "UDR", "ULTA", "USB", "UAA", "UA", "UNP", "UAL", "UNH", "UPS", "URI", "UHS", "UNM", "VLO", "VTR", "VRSN", "VRSK", "VZ", "VRTX", "VFC", "VIAC", "VTRS", "V", "VNO", "VMC", "WRB", "WAB", "WMT", "WBA", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WU", "WRK", "WY", "WHR", "WMB", "WLTW", "WYNN", "XRAY", "XOM", "XEL", "XLNX", "XYL", "YUM", "ZBRA", "ZBH", "ZION", "ZTS"]
#llamada a la API de yahoo
print("Se ha comenzado la polulacion de la base de datos: {}:{}".format(datetime.now().hour, datetime.now().minute))
contador = 0

for ticker in tickers:
    asset_kwargs = {}
    data = Ticker(ticker)
    try:
        contador += 1
        print(contador, ticker)
        asset_kwargs['ticker'] = ticker
        asset_kwargs['exchange'] = data.quote_type[ticker].get('exchange') 
        asset_kwargs['name'] = data.quote_type[ticker].get('longName')
        asset_kwargs['asset_type'] =data.quote_type[ticker].get('quoteType')
        asset_kwargs['sector'] = data.asset_profile[ticker].get('sector')
    except:
        pass
    asset = Asset(**asset_kwargs)
    try:
        storage.new(asset)
        storage.save()
    except: 
        print("No se pudo grabar el objeto", ticker)

print("Se ha terminado la polulacion de la base de datos: {}:{}".format(datetime.now().hour, datetime.now().minute))
print("DataBase have been pollulated")
storage.close()



