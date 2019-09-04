from CRABClient.UserUtilities import config
config = config()

config.General.transferLogs = False

config.JobType.pluginName = "ANALYSIS"

config.Data.outLFNDirBase = "/store/group/lpcsusystealth/privateMCProduction/"
config.Data.inputDataset = ""
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.outputPrimaryDataset = "SMS-T5WgStealth_PrivateProduction_13TeV-madgraphMLM-pythia8"
config.Data.userInputFiles = PLACEHOLDER
config.Data.totalUnits = len(config.Data.userInputFiles)

config.Site.storageSite = "T3_US_FNALLPC"
