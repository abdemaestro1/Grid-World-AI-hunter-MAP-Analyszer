def main():
    def file_normelize(file_name):
        open_file=open(file_name,"r")
        finished_list=[]
        for line in open_file: #Must be read all the lines not a NUM 
            clean_line=line.strip().replace(",","").lower()
            file_reader=clean_line.split()
            finished_list.append(file_reader)
        #Make the average words
        total_words=0.0
        for i in finished_list:
            total_words+=len(i)
        num_lines=len(finished_list)
        average_words=total_words/num_lines

        #EXtract the begining of every word and sort it 
        words_list=[]
        for x in finished_list:
            for y in x:
                words_list.append(y)
        words_list.sort()

        #make adocument signature
        Documents_signature=[]
        for x in words_list:
            if len(x)>=5:
                Documents_signature.append(x[0])
        print(Documents_signature)
        open_file.close()
        #Task 5:last touch make a new file and fill it with your report
        output_file = open("summary_report.txt", "w")
        
        print("=== DOCUMENT ANALYSIS REPORT ===", file=output_file)
        print(f"Total Line Count: {num_lines}", file=output_file)
        print(f"Total Word Count: {total_words}", file=output_file)
        print(f"Average Word Length: {average_words:.2f}", file=output_file)
        print(f"Document Acronym Signature: {Documents_signature}", file=output_file)
        print("\n--- Sorted Unique Vocabulary ---", file=output_file)

        output_file.close()
        print("Report successfully generated in summary_report.txt!")
    file_normelize("input_text.txt")

main()