FROM nimlang/nim:latest-alpine

COPY . .
RUN nimble install
RUN nimble build
RUN ls

CMD ["./AdventOfCode2020"]
