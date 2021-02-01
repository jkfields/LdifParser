
"""
.. codeauthor:: Jeffrey Fields <jkfields@yahoo.com>
"""

class LdifParsingException(Exception):
    pass

class LdifParser:
    def parse(self, ldifattrs)
        """
        parse the ldif attribute data received from an ldapsearch
        query against a Sun/Oracle Directory Server
      
        :: each record can have multiple values for a single attribute
        :: each record is separated by a blank line
        :: attributes are colon-separated; some values are also
           colon separated; split line on 1st colon
        """
        try:
            # process each line of the block of data
            for ln in ldifattrs.split('\n'):
                if not rec in locals():  rec = {}
                
                # is this the blank line?
                if ln.strip():
                    # attr and value are colon-separated; some values are also comma separate; 
                    # split on the 1st colon in the string
                    attr, value = [ str.strip() for str in ln.split(':', 1) ]
                    
                    # convert and numeric strings to int
                    if value.isdigit():  value = int(value)
                    # convert true/false strings to boolean
                    elif value.lower() == 'true':  value = True
                    elif value.lower() == 'false':  value = False
                    # convert date string to ISO-8601 formatted string
                    elif "Time" in attr:  value = dtToIso(value)
                    
                    # check for additional values for existing attrs
                    if attr in rec.keys():
                        # if first duplicate, converts dict value to list
                        if not isinstance(rec.get(attr), list):
                            rec[attr] = [ lrec.get(attr) ]
                            
                            # append the new value
                            rec[attr].append(value)
                    else:
                        # add the attr and value to the dict
                        rec[attr] = value
                else:
                    yield rec
                    rec.clear()
                    
        except Exception as err:
            raise LdifParsingException(err)
    
    @staticmethod
    def dtToIso(dtstr):
        # TODO:  parse string using pure python based on python 2.6.5
        return dtstr
        
