# TPP
#### Project for informational unification of the public transport in Portugal

[![Contributing Guidelines](https://img.shields.io/badge/%E2%9D%A4-Contributing%20Guidelines-blue.svg)](https://github.com/tpportugal/tpp/blob/master/CONTRIBUTING_EN.md)
[![Communication Channel](https://img.shields.io/badge/Communication%20Channel-Slack-orange.svg)]((https://join.slack.com/t/tpportugal/shared_invite/enQtMzEwOTI3ODg0MDk2LTZmNjYxOWVmZTBkN2EwNWUzMGFhOGQ2MWM0YmQ4NGUxMTU1ZjcwMDQxMDljMzU0Njg0ODcwOGIyODUxMjIzNmI))
[![Administrators](https://img.shields.io/badge/Administrators-3-red.svg)](https://github.com/tpportugal/tpp/blob/master/ADMINS.md)

***

## Goal

This project aims to unify all of the public transport in Portugal in a single application, that is, the unification of types of transport, schedules and routes in a single system so that the user, in this case, the traveler can move in Portugal with greater ease with only introducing the place of departure and the place of arrival.

## How it works

So that the application can show the best route between point A and point B it is necessary to have in our possession several types of data such as: Regions, Routes, Types of transport, Operators and Timetables. From this data our algorithm will be able to calculate the most efficient route for the user, that is, that has the least number of line changes, as well as the duration of the trip. Obviously it is also necessary that the data is updated as communicated by the operators.

## Data collection

Usually by digital channels where the operators have their data published. There will be cases where the operators do not have schedules in digital format, there we have to do a scan of the schedules and apply a pattern recognition algorithm that extracts the data for us, this to avoid human errors in the data entry.

# Services

**Valhalla** [Routing engine] - https://github.com/tpportugal/tpp_valhalla  
**Datastore** [TPP Centralized Web Service API] - https://github.com/tpportugal/tpp_banco_de_dados  
**Explorer** [Explorer of transport networks in Portugal] - https://github.com/tpportugal/tpp_explorador  
**APP** [Frontend for the TPP service] - https://github.com/tpportugal/tpp_app  
**Dispatcher** [Backend Administrator for Datastore] - https://github.com/tpportugal/tpp_expedidor  
**Feed Registry** [Operator feeds directory] - https://github.com/tpportugal/tpp_registo_de_feeds  
**Admin** [Django TPP Admin management project] - https://github.com/tpportugal/tpp_admin  
