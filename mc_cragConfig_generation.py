from CRABClient.UserUtilities import config
config = config()

config.General.transferLogs = False

config.JobType.pluginName = "PRIVATEMC"

config.Data.outLFNDirBase = "/store/group/lpcsusystealth/privateMCProduction/"
config.Data.inputDataset = ""
config.Data.splitting = "EventBased"
config.Data.outputPrimaryDataset = "SMS-T5WgStealth_PrivateProduction_13TeV-madgraphMLM-pythia8"

config.Site.storageSite = "T3_US_FNALLPC"
