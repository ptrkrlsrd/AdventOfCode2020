FROM mcr.microsoft.com/dotnet/sdk:5.0 as build

WORKDIR /app

COPY . .
RUN [ "dotnet", "build"]
RUN ["dotnet", "publish", "-c", "Release", "-o", "out"]


FROM mcr.microsoft.com/dotnet/sdk:5.0
COPY --from=build /app/out .
ENTRYPOINT ["dotnet", "Day03.dll"]