import json
from base.src.models import UnassignedFreq
from base.src.arfcn import FreqRangeToArfcnRange


class pawscFunction:
    """"""
    def get_spectrum ():
        """
        json dump output is of the form: [{"freqend": <value>, "freqstart": <value>}, {"freqend": <value>, "freqstart": <value>}, ...]
        """       
        
        #return json.dumps([dict(item) for item in UnassignedFreq.objects.all().values("freqstart", "freqend")])
        
        #return UnassignedFreq.objects.all().values("freqstart", "freqend") #returns raw unassigned start and stop frequecy ranges
        #return FreqRangeToArfcnRange('900E','GSM',880,885,0.2)
        
        freq_ranges = []
       # freq_ranges = UnassignedFreq.objects.all().values("freqstart", "freqend")
       
        
        for item in UnassignedFreq.objects.all().values("freqstart", "freqend"):
            print (item['freqstart'], item['freqend'])
            freq_ranges.append(FreqRangeToArfcnRange('900E','GSM', item['freqstart'], item['freqend'] ,0.2))
            FreqRangeToArfcnRange('900E','GSM', item['freqstart'], item['freqend'] ,0.2)
         
        #print (freq_ranges)
        #for item in UnassignedFreq.objects.all().values("freqstart", "freqend"):
            #print item
        #item = (880, 885)
        #return (FreqRangeToArfcnRange('900E','GSM',item[0], item[1], 0.2) )
        return freq_ranges
        """
        May need to strip off the brackets depending on output format requirements
        """    
        #return str(freq_ranges).strip("[ ]")
       
        

    def __init__(self):
        """Constructor"""
        
        
    
    