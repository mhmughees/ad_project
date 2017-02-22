


def change_file(f):
    cust= open('/Users/mhmughees/Downloads/pets_adblock_work/ad_project/cust_nocss.txt','a+')
    for row in f:
        if "##" not in row:
            cust.write(row)

if __name__ == "__main__":
    f= open('/Users/mhmughees/Downloads/pets_adblock_work/ad_project/cust_easylist.txt')
    change_file(f)


