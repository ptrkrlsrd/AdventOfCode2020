FROM nimlang/nim:latest-alpine

COPY . .
RUN nimble install
RUN nimble build

CMD ["./AdventOfCode2020"]
