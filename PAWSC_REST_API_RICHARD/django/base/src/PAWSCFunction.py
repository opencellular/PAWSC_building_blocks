"""
This file contains essential functions to process pawsc requests
"""
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
       
        data = UnassignedFreq.objects.all().values("freqstart", "freqend").filter(band = 900)
        freq_ranges = []
        freq_ranges_Hz = []
        for item in data: #UnassignedFreq.objects.all().values("freqstart", "freqend"):
            #print (item['freqstart'], item['freqend'])
            freq_ranges.append(FreqRangeToArfcnRange(freq_band,tech, item['freqstart'], item['freqend'], bw))
            #FreqRangeToArfcnRange(freq_band,tech, item['freqstart'], item['freqend'] , bw)
            freq_ranges_Hz.append({'freqstart': item['freqstart']*1000000, 'freqend': item['freqend']*1000000})
        #print (freq_ranges)
        #for item in UnassignedFreq.objects.all().values("freqstart", "freqend"):
            #print item
        #item = (880, 885)
        #return (FreqRangeToArfcnRange('900E','GSM',item[0], item[1], 0.2) ) 
        '''
        Attempting to format the frequency ranges in a way client expects
        '''
        arfcn = []
        for item in freq_ranges:
            #print ("DARFCN:", item['arfcn_start']['arfcn_DL'], "UARFCN:", item['arfcn_start']['arfcn_UL'], "Ddbm:  30.0, Udbm: 20.0" )
            arfcn.append({"DARFCN": item['arfcn_start']['arfcn_DL'], "UARFCN": item['arfcn_start']['arfcn_UL'], "Ddbm": 30.0, "Udbm": 20.0})
            arfcn.append({"DARFCN": item['arfcn_end']['arfcn_DL'], "UARFCN": item['arfcn_end']['arfcn_UL'], "Ddbm": 30.0, "Udbm": 20.0})        
              
         
        return freq_ranges_Hz, "profilesN", arfcn
        """
        May need to strip off the brackets depending on output format requirements
        """    
        #return str(freq_ranges).strip("[ ]")      
        

    def __init__(self):
        """Constructor"""
        
        
    
    