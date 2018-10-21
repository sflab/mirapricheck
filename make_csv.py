from dataset.mirapri_retriever import MiraPriRetriever

START=4000
END=20000
INTERVAL=1000

for head in range(START, END, INTERVAL):
    retriever = MiraPriRetriever(1)
    retriever.get(range(head, head + INTERVAL))
    filename="data/{}_{}.csv".format(head, head + INTERVAL)
    retriever.to_csv(filename)
