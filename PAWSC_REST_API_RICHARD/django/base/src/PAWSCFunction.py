import json
from base.src.models import UnassignedFreq
from base.src.arfcn import FreqRangeToArfcnRange


class pawscFunction:
    """"""
    def get_spectrum (freq_band,tech,bw):
        """
        json dump output is of the form: [{"freqend": <value>, "freqstart": <value>}, {"freqend": <value>, "freqstart": <value>}, ...]
        """       
        
        #return json.dumps([dict(item) for item in UnassignedFreq.objects.all().values("freqstart", "freqend")])
        
        #return UnassignedFreq.objects.all().values("freqstart", "freqend") #returns raw unassigned start and stop frequecy ranges
        #return FreqRangeToArfcnRange('900E','GSM',880,885,0.2)
        """
        To fetch all:
        UnassignedFreq.objects.all().values("freqstart", "freqend")
        
        To fetch subset e.g. for specific band:          
        if (freq_band == '900E' ):
            data = UnassignedFreq.objects.all().values("freqstart", "freqend").filter(band = 900)
        """      
       
        data = UnassignedFreq.objects.all().values("freqstart", "freqend")
        freq_ranges = []     
        for item in data: #UnassignedFreq.objects.all().values("freqstart", "freqend"):
            print (item['freqstart'], item['freqend'])
            freq_ranges.append(FreqRangeToArfcnRange(freq_band,tech, item['freqstart'], item['freqend'], bw))
            FreqRangeToArfcnRange(freq_band,tech, item['freqstart'], item['freqend'] , bw)
         
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
        
        
    
    