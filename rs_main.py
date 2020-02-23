## Library
#

## Main
#---- Re-include
import importlib as imp
import rs_global
import rs_class_trading_total
imp.reload(rs_global)
imp.reload(rs_class_trading_total)
from rs_class_trading_total import *
from rs_global import *

#---- Main code
def main() :
   class_trading_total_call = class_trading_total()
   cur_path, input_path, output_path,  = get_path(add_dir_path='/price_trend_by_KB/month')
   path_month_price_trend = input_path
   filename_month_price_trend = '/★(월간)KB주택가격동향_시계열(2020.01)44552931708064728.xlsx'
   class_trading_total_call.def_main(path_month_price_trend, filename_month_price_trend)


#----------------------------
if __name__ == '__main__' :
   start_timer()
   main()
   end_timer()




