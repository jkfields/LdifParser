
"""
.. codeauthor:: Jeffrey Fields <jkfields@yahoo.com>
"""

class LdifParser:
  def parse(self, ldifattrs):
      """
      parse the ldif attribute data received from an ldapsearch
      query against a Sun/Oracle Directory Server
      
      each record can have multiple values for a single attribute
      each record is separated by a blank line
      """
      try:
        # process each line of the block of data
        for ln in ldifattrs.split('\n'):
          if not rec in locals():  rec = {}
          
          # is this the blank line?
          if ln.strip():
              # the attr and value are colon-separated
              attr, value = [ str.strip() for str in ln.split(':', 1) ]
            
              # convert and number values to int
              # convers any boolean values
              if value.isdigit():  value = int(value)
              elif value.lower() == 'true':  value = True
              elif value.lower() == 'false':  value = False
              elif "Time" in attr:  value = dtToIso(value)
              else:  pass
