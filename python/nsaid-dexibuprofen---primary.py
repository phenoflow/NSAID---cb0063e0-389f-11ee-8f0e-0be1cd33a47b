# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"10149","system":"gprdproduct"},{"code":"10325","system":"gprdproduct"},{"code":"1086","system":"gprdproduct"},{"code":"11461","system":"gprdproduct"},{"code":"11907","system":"gprdproduct"},{"code":"12709","system":"gprdproduct"},{"code":"1392","system":"gprdproduct"},{"code":"14333","system":"gprdproduct"},{"code":"1468","system":"gprdproduct"},{"code":"15","system":"gprdproduct"},{"code":"16001","system":"gprdproduct"},{"code":"19046","system":"gprdproduct"},{"code":"26095","system":"gprdproduct"},{"code":"2622","system":"gprdproduct"},{"code":"26970","system":"gprdproduct"},{"code":"27782","system":"gprdproduct"},{"code":"27783","system":"gprdproduct"},{"code":"28348","system":"gprdproduct"},{"code":"29316","system":"gprdproduct"},{"code":"29332","system":"gprdproduct"},{"code":"29345","system":"gprdproduct"},{"code":"29352","system":"gprdproduct"},{"code":"2938","system":"gprdproduct"},{"code":"29749","system":"gprdproduct"},{"code":"30243","system":"gprdproduct"},{"code":"30382","system":"gprdproduct"},{"code":"32100","system":"gprdproduct"},{"code":"32242","system":"gprdproduct"},{"code":"32509","system":"gprdproduct"},{"code":"32862","system":"gprdproduct"},{"code":"32875","system":"gprdproduct"},{"code":"33589","system":"gprdproduct"},{"code":"33704","system":"gprdproduct"},{"code":"34354","system":"gprdproduct"},{"code":"34359","system":"gprdproduct"},{"code":"34425","system":"gprdproduct"},{"code":"34447","system":"gprdproduct"},{"code":"34527","system":"gprdproduct"},{"code":"34536","system":"gprdproduct"},{"code":"34550","system":"gprdproduct"},{"code":"34621","system":"gprdproduct"},{"code":"34663","system":"gprdproduct"},{"code":"34729","system":"gprdproduct"},{"code":"34757","system":"gprdproduct"},{"code":"34850","system":"gprdproduct"},{"code":"34889","system":"gprdproduct"},{"code":"34911","system":"gprdproduct"},{"code":"34931","system":"gprdproduct"},{"code":"34961","system":"gprdproduct"},{"code":"34980","system":"gprdproduct"},{"code":"3599","system":"gprdproduct"},{"code":"36597","system":"gprdproduct"},{"code":"392","system":"gprdproduct"},{"code":"39354","system":"gprdproduct"},{"code":"39502","system":"gprdproduct"},{"code":"40083","system":"gprdproduct"},{"code":"40253","system":"gprdproduct"},{"code":"41513","system":"gprdproduct"},{"code":"416","system":"gprdproduct"},{"code":"41701","system":"gprdproduct"},{"code":"42108","system":"gprdproduct"},{"code":"4309","system":"gprdproduct"},{"code":"43911","system":"gprdproduct"},{"code":"44730","system":"gprdproduct"},{"code":"45216","system":"gprdproduct"},{"code":"45320","system":"gprdproduct"},{"code":"45331","system":"gprdproduct"},{"code":"45842","system":"gprdproduct"},{"code":"46921","system":"gprdproduct"},{"code":"46942","system":"gprdproduct"},{"code":"48062","system":"gprdproduct"},{"code":"48084","system":"gprdproduct"},{"code":"48138","system":"gprdproduct"},{"code":"48326","system":"gprdproduct"},{"code":"48546","system":"gprdproduct"},{"code":"48562","system":"gprdproduct"},{"code":"48644","system":"gprdproduct"},{"code":"4911","system":"gprdproduct"},{"code":"49266","system":"gprdproduct"},{"code":"49277","system":"gprdproduct"},{"code":"50266","system":"gprdproduct"},{"code":"50628","system":"gprdproduct"},{"code":"50652","system":"gprdproduct"},{"code":"51614","system":"gprdproduct"},{"code":"51828","system":"gprdproduct"},{"code":"52009","system":"gprdproduct"},{"code":"52154","system":"gprdproduct"},{"code":"52617","system":"gprdproduct"},{"code":"53331","system":"gprdproduct"},{"code":"53604","system":"gprdproduct"},{"code":"53803","system":"gprdproduct"},{"code":"54137","system":"gprdproduct"},{"code":"55233","system":"gprdproduct"},{"code":"55313","system":"gprdproduct"},{"code":"55434","system":"gprdproduct"},{"code":"56039","system":"gprdproduct"},{"code":"56213","system":"gprdproduct"},{"code":"5648","system":"gprdproduct"},{"code":"57112","system":"gprdproduct"},{"code":"586","system":"gprdproduct"},{"code":"58652","system":"gprdproduct"},{"code":"59067","system":"gprdproduct"},{"code":"59553","system":"gprdproduct"},{"code":"59562","system":"gprdproduct"},{"code":"60035","system":"gprdproduct"},{"code":"647","system":"gprdproduct"},{"code":"784","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nsaid-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nsaid-dexibuprofen---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nsaid-dexibuprofen---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nsaid-dexibuprofen---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
