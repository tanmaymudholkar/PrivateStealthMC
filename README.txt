# Generating FastSim and FullSim Stealth Fall17MC samples
# NOTE: Requires SLC6 machine

# Fall17MC, FastSim
export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_4_12/src
# Stealth gen fragment: https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SUS-RunIIFall17FSPremix-00069
# NOTES: The gen fragment below only corresponds to T5WgStealth_1000_500, i.e. m_glu = 1000 GeV, m_chi = 500 GeV
#        Stealth gen fragment below uses pythia8CP2Settings for multi-parton interactions in Pythia8GeneratorFilter
#            whereas HIG-RunIIFall17 campaign uses pythia8CP5Settings
#        Stealth gen fragment below uses 'JetMatching:qCut = 140.' for jet-parton matching in Pythia8GeneratorFilter
#            whereas HIG-RunIIFall17 campaign uses 'JetMatching:qCut = 30.'
#        The LHE gridpack should allow for N_events = 150k to be generated
# GEN to AOD
cmsRun SUS-RunIIFall17FSPremix-00069_1_cfg.py
# AOD to MINIAOD
cmsRun SUS-RunIIFall17MiniAODv2-00332_1_cfg.py

# Fall17MC, FullSim
# Emulates HIG-RunIIFall17, TuneCP5
# NOTES: The gen fragment below only corresponds to T5WgStealth_1000_500, i.e. m_glu = 1000 GeV, m_chi = 500 GeV
#        Stealth gen fragment below uses pythia8CP5Settings for multi-parton interactions in Pythia8GeneratorFilter
#        Stealth gen fragment below uses 'JetMatching:qCut = 140.' for jet-parton matching in Pythia8GeneratorFilter
#            whereas HIG-RunIIFall17 campaign uses 'JetMatching:qCut = 30.'
export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_9_4_7/src
# GEN to SIM
cmsRun SUS-RunIIFall17wmLHEGS-00069_1_cfg.py
# SIM to RAW
cmsRun SUS-RunIIFall17DRPremix-00069_1_cfg.py
# RAW to AOD
cmsRun SUS-RunIIFall17DRPremix-00069_2_cfg.py
# AOD to MINIAOD
cmsRun SUS-RunIIFall17MiniAODv2-00069_1_cfg.py

# For CRAB production, some useful parameters to set:
# NOTE: CRAB sets an upper limit on the allowed number of jobs to be submitted in a single submission
        of config.Data.totalUnits/config.Data.unitsPerJob <= 10e3
# For first (generation) step:
config.JobType.psetName = 'cms_cfg.py'
config.Data.splitting = 'FileBased'
config.Data.totalUnits = 150e3
config.Data.outputPrimaryDataset = 'SMS-T5WgStealth_TuneCP2_13TeV-madgraphMLM-pythia8' # or CP5
# where cms_cfg.py = SUS-RunIIFall17FSPremix-00069_1_cfg.py (FastSim) or SUS-RunIIFall17wmLHEGS-00069_1_cfg.py (FullSim) 

# For subsequent steps:
config.JobType.psetName = 'cms_cfg.py'
config.Data.splitting = 'FileBased'
config.Data.outputPrimaryDataset = 'SMS-T5WgStealth_TuneCP2_13TeV-madgraphMLM-pythia8' # or CP5
# If dataset is not published:
config.Data.userInputFiles = open('input_file_list_index.txt').readlines()
config.Data.totalUnits = len(config.Data.userInputFiles)
# If dataset is published:
config.Data.inputDBS = 'phys03' # user-submitted datasets are published to phys03 by default
config.Data.inputDataset = '/<primaryDataset>/<datasetName>/USER'
# where cms_cfg.py corresponds to the cms cfg file for the subsequent steps
#       input_file_list_index.txt contains a list of the output files (one file per line) from the previous step
#           prefixed by the redirector corresponding to where the files are stored, i.e. root://cmseos.fnal.gov//store/to/file.root (FNAL)
#           or root://eoscms.cern.ch//eos/cms/store/to/file.root (LXPLUS)
#       <primaryDataset> corresponds to the config.Data.outputPrimaryDataset of the input dataset, see CRAB log
#       <datasetName> can be found in the CRAB log of the input submission

