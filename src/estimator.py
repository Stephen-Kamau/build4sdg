def estimator(data):
    # resuldts format
    # { data: {},  impact: {},  severeImpact: {}}

    # input format
#     {
#  region: {
#  name: "Africa",
#  avgAge: 19.7,
#  avgDailyIncomeInUSD: 5,
#  avgDailyIncomePopulation: 0.71
#  },
#  periodType: "days",
#  timeToElapse: 58,
#  reportedCases: 674,
#  population: 66622705,
#  totalHospitalBeds: 1380614
# }


##3Challenge 1
    # get input data ...impact estaimation and severe impact estaimation
    results = {'data':data, 'impact': {}, 'severeImpact': {}}
    #use indexing to place the data for results
    #inside impact datastructure
    results['impact']['currentlyInfected'] = data['reportedCases'] * 10
    # for severe impact
    results['severeImpact']['currentlyInfected'] = data['reportedCases'] * 50
    #we have to check types of period given from data in the periodType
    # for weeks set the number of days to elapse months ==times 7
    if data['periodType'] == 'weeks':
        data['timeToElapse'] = data['timeToElapse'] * 7
        # times 30
    elif data['periodType'] == 'months':
        data['timeToElapse'] = data['timeToElapse'] * 30
#impacts
    results['impact']['infectionsByRequestedTime'] = results['impact']['currentlyInfected'] * (2 ** (data['timeToElapse']//3))
    results['severeImpact']['infectionsByRequestedTime'] = results['severeImpact']['currentlyInfected'] * (2 ** (data['timeToElapse']//3))

#Challenge 2
# we start with 15%
    results['impact']['severeCasesByRequestedTime'] = int(0.15 * (results['impact']['infectionsByRequestedTime']))
    results['severeImpact']['severeCasesByRequestedTime'] = int(0.15 * (results['severeImpact']['infectionsByRequestedTime']))
#bed estimation hospital
#0.65 are occupied thus 0.35 will be available
    results['impact']['hospitalBedsByRequestedTime'] = int((0.35 * (data['totalHospitalBeds'])) - results['impact']['severeCasesByRequestedTime'])
    results['severeImpact']['hospitalBedsByRequestedTime'] = int((0.35 * (data['totalHospitalBeds'])) - results['severeImpact']['severeCasesByRequestedTime'])


#challenge 3
#those needing icu care
    results['impact']['casesForICUByRequestedTime'] = int(0.05 * results['impact']['infectionsByRequestedTime'])
    results['severeImpact']['casesForICUByRequestedTime'] = int(0.05 * results['severeImpact']['infectionsByRequestedTime'])
    #those neeeding ventilator
    results['impact']['casesForVentilatorsByRequestedTime'] = int(2/100 * results['impact']['infectionsByRequestedTime'])
    results['severeImpact']['casesForVentilatorsByRequestedTime'] = int(2/100 * results['severeImpact']['infectionsByRequestedTime'])
#loss incurred by the epidemic
    results['impact']['dollarsInFlight'] = int((results['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation']) /data['timeToElapse'])
    results['severeImpact']['dollarsInFlight'] = int((results['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'])/data['timeToElapse'])
#return the calculated results
    return results




#testing the function if it performs welss
data1 = {
  'region':{
    'name':'Africa',
    'avgAge':19.7,
    'avgDailyIncomeInUSD':5,
    'avgDailyIncomePopulation':0.71
  },
    'periodType':'days',
    'timeToElapse':58,
    'reportedCases':674,
    'population':66622705,
    'totalHospitalBeds':1380614
}
test1 = estimator(data1)
print(test1)

data2 = {
  'region':{
    'name':'America',
    'avgAge':25.1,
    'avgDailyIncomeInUSD':40,
    'avgDailyIncomePopulation':0.94
  },
    'periodType':'weeks',
    'timeToElapse':5,
    'reportedCases':2577,
    'population':3873959,
    'totalHospitalBeds':298349
}
test2 = estimator(data2)
print(test2)
