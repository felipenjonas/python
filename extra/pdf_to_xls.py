import tabula

arquivo = tabula.read_pdf("./planilhas_dataset_IEB_USP.pdf", pages="all")


tabula.convert_into("./planilhas_dataset_IEB_USP.pdf", "./dataset_IEB.csv", output_format="csv", pages="all")