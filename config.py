
# ---Specify here header/footer keyword to be removed, using the  --keep_header flag removes the effect
header_keyword=["K C Tang Consultants Ltd.", "OFFICE RENOVATION FOR HKSAPID AT", "OFFICE RENOVATION FOR HKSAPID AT", "SCHEDULE OF WORKS", "SCHEDULE NO. 1 - PRELIMINARIES", "LEK YUEN COMMUNITY HALL, SHATIN, NT", "UNIT NO. 2+7, G/F", "SCHEDULE NO.", "LEK YUEN COMMUNITY HALL,SHAUN, NT", "KTang Consultants Ltd", "UNIT NO. +7, G/F", "LEK WEN COMMUNITY HALL, SHATIR NT", "Summary of Tender", "LEK YUEN COMMUNITY HALL, SHATIN, NT.", "OFFICE RENOVATION OF HKSAPJD AT", "E&M installation","Summary","785HKSAPID SOW", "LEK YUEN COMMUNITY HALL, SHAT N, NT","g/ro.ttci £LYJ", "LEK YUEN COMMUNITY HALL, SHATiN, NT", "KTang Consultants Ltd.", "KC Tang Consultants Ltd.","LEK YUEN COMMUNITY HALL, SHATINNT", "785SOW", "KC Tang Consultants Ltd", "LEK YUEN COMMUNITY HALLSHATIN, NT", "785HKSAPID SOW", "i", "/", ". V"]


# ---Specify here header/footer keyword where rows that contains them will be removed, using the the --keep_header flag ignores header removoal
header_contain=["HKSAPID_SOW", "HKSAPIDSOW", "SCHEDULE NO.", "TENDER ADDENDUM","HKSAP!DSOW", "TENDER ADDENDUM NO. 2", "TENDER ADDENDUM NO. 2", "Submitted by:", "UNIT NO.2+7,G/F .", "Submitted by", "UNIT NO."]

#----REMOVE words that are exact match as the following words
# Capitalization matters
remove_items=["item", "Item"]

# ---Remove all occurence of table heads that is not the first occurence
#remove_table_head

#---Further format
# --- If first column contain the following characters, move the next column numbers to the first column.
column_list=["2/", "5/"]
