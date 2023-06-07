FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["SpotifySyncer/SpotifySyncer.csproj", "SpotifySyncer/"]
RUN dotnet restore "SpotifySyncer/SpotifySyncer.csproj"
COPY . .
WORKDIR "/src/SpotifySyncer"
RUN dotnet build "SpotifySyncer.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SpotifySyncer.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SpotifySyncer.dll"]
