""""
def main():
  raw_log = "104-101-108-108-111 |  #SYS_LOG#  |  32-87-111-114-108-100!  | ERROR_404"
  field1,field2,field3,field4=raw_log.split("|")  
  decoded_one=field1.split("-")
  final_message=[]
  for i in decoded_one:
    intVAR=int(decoded_one[i])
    asciVAR=chr(intVAR)
    final_message=final_message.append(asciVAR)
  print(final_message)
main()
"""
def main():
  raw_log ="104-101-108-108-111 | #SYS\_LOG# | 32-87-111-114-108-100! | ERROR_404"
  field1,field2,field3,field4=raw_log.split("|")
  field1=field1.strip()
  field2=field2.strip()
  field3=field3.strip()
  field4=field4.strip()

  def decoded_code(field):
    clean=""
    for i in field:
      if i.isdigit() or i == '-':
        clean+=i
    clean=clean.split("-")
    clean_version=[]
    for i in clean:
      clean_version.append(chr(int(i)))
    return ''.join(clean_version)
  decoded_code(field1)      
main()

