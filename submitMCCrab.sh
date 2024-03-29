#!/bin/bash

BASEHOSTNAME=$(echo $HOSTNAME | sed "s|\([^\.]*\)\.cern\.ch|\1|" | sed "s|\([^\.]*\)\.fnal\.gov|\1|")
if [[ "${BASEHOSTNAME}" =~ ^lxplus[0-9]{3,4}$ ]]; then
    echo "Not implemented yet for lxplus!"
    exit 1
fi
export X509_USER_PROXY=${HOME}/private/x509up_u$(id -u)
source ${HOME}/.fnal_bashrc

CFGFILESSOURCE="/uscms/home/tmudholk/private/stealth/stealthMC/production_configs"
cd ${CFGFILESSOURCE}

CMSSWSOURCE=""
CRABOPTIONS=""
CRABCONFIGFILE=""
case "${1}" in
    fastsim)
	echo "Submitting crab job for fastsim"
	CMSSWSOURCE="/uscms/home/tmudholk/private/stealth/stealthMC/CMSSW_9_4_12/src"
	case "${2}" in
	    1)
		echo "Step: 1"
		CMSSWCFGFILE="fastsim_step1_cfg.py"
		CRABOPTIONS="General.requestName=job_${1}_step${2} General.workArea=crab_workArea_job_${1}_step${2} JobType.psetName=${CMSSWCFGFILE} JobType.eventsPerLumi=501 Data.totalUnits=150e3 Data.unitsPerJob=501"
		CRABCONFIGFILE="mc_crabConfig_generation.py"
		;;
	    2)
		echo "Step: 2"
		CMSSWCFGFILE="fastsim_step2_cfg.py"
		CRABOPTIONS="General.requestName=job_${1}_step${2} General.workArea=crab_workArea_job_${1}_step${2} JobType.psetName=${CMSSWCFGFILE}"
		CRABCONFIGFILE="mc_crabConfig_reco_${1}_step${2}.py"
		echo "Building list of input files..."
		rec_eosls "/store/group/lpcsusystealth/privateMCProduction/SMS-T5WgStealth_PrivateProduction_13TeV-madgraphMLM-pythia8/crab_job_${1}_step1" | tee inputFilesList_raw_${1}_step${2}.txt && cat inputFilesList_raw_${1}_step${2}.txt | grep -v "failed" | grep ".root" | sed "s|/store/|${EOSPREFIX}/store/|" > inputFilesList_${1}_step${2}.txt && rm inputFilesList_raw_${1}_step${2}.txt
		echo "Building CRAB config file..."
		sed "s|userInputFiles = PLACEHOLDER|userInputFiles = open(\"inputFilesList_${1}_step${2}.txt\").readlines()|" mc_crabConfig_reco.py > ${CRABCONFIGFILE}
		;;
	    *)
		echo "Unrecognized second argument. Should be either 1 or 2 for the fastsim step number. Currently: ${2}"
		exit 1
	esac
	;;
    fullsim)
	echo "Submitting crab job for fullsim"
	CMSSWSOURCE="/uscms/home/tmudholk/private/stealth/stealthMC/CMSSW_9_4_12/src"
	case "${2}" in
	    1)
		echo "Step: 1"
		CMSSWCFGFILE="fullsim_step1_cfg.py"
		CRABOPTIONS="General.requestName=job_${1}_step${2} General.workArea=crab_workArea_job_${1}_step${2} JobType.psetName=${CMSSWCFGFILE} JobType.eventsPerLumi=101 Data.totalUnits=150e3 Data.unitsPerJob=101"
		CRABCONFIGFILE="mc_crabConfig_generation.py"
		;;
	    2)
		echo "Step: 2"
		CMSSWCFGFILE="fullsim_step2_cfg.py"
		CRABOPTIONS="General.requestName=job_${1}_step${2} General.workArea=crab_workArea_job_${1}_step${2} JobType.psetName=${CMSSWCFGFILE}"
		CRABCONFIGFILE="mc_crabConfig_reco_${1}_step${2}.py"
		echo "Building list of input files..."
		rec_eosls "/store/group/lpcsusystealth/privateMCProduction/SMS-T5WgStealth_PrivateProduction_13TeV-madgraphMLM-pythia8/crab_job_${1}_step1" | tee inputFilesList_raw_${1}_step${2}.txt && cat inputFilesList_raw_${1}_step${2}.txt | grep -v "failed" | grep ".root" | sed "s|/store/|${EOSPREFIX}/store/|" > inputFilesList_${1}_step${2}.txt && rm inputFilesList_raw_${1}_step${2}.txt
		echo "Building CRAB config file..."
		sed "s|userInputFiles = PLACEHOLDER|userInputFiles = open(\"inputFilesList_${1}_step${2}.txt\").readlines()|" mc_crabConfig_reco.py > ${CRABCONFIGFILE}
		;;
	    3)
		echo "Step: 3"
		CMSSWCFGFILE="fullsim_step3_cfg.py"
		CRABOPTIONS="General.requestName=job_${1}_step${2} General.workArea=crab_workArea_job_${1}_step${2} JobType.psetName=${CMSSWCFGFILE}"
		CRABCONFIGFILE="mc_crabConfig_reco_${1}_step${2}.py"
		echo "Building list of input files..."
		rec_eosls "/store/group/lpcsusystealth/privateMCProduction/SMS-T5WgStealth_PrivateProduction_13TeV-madgraphMLM-pythia8/crab_job_${1}_step2" | tee inputFilesList_raw_${1}_step${2}.txt && cat inputFilesList_raw_${1}_step${2}.txt | grep -v "failed" | grep ".root" | sed "s|/store/|${EOSPREFIX}/store/|" > inputFilesList_${1}_step${2}.txt && rm inputFilesList_raw_${1}_step${2}.txt
		echo "Building CRAB config file..."
		sed "s|userInputFiles = PLACEHOLDER|userInputFiles = open(\"inputFilesList_${1}_step${2}.txt\").readlines()|" mc_crabConfig_reco.py > ${CRABCONFIGFILE}
		;;
	    4)
		echo "Step: 4"
		CMSSWCFGFILE="fullsim_step4_cfg.py"
		CRABOPTIONS="General.requestName=job_${1}_step${2} General.workArea=crab_workArea_job_${1}_step${2} JobType.psetName=${CMSSWCFGFILE}"
		CRABCONFIGFILE="mc_crabConfig_reco_${1}_step${2}.py"
		echo "Building list of input files..."
		rec_eosls "/store/group/lpcsusystealth/privateMCProduction/SMS-T5WgStealth_PrivateProduction_13TeV-madgraphMLM-pythia8/crab_job_${1}_step3" | tee inputFilesList_raw_${1}_step${2}.txt && cat inputFilesList_raw_${1}_step${2}.txt | grep -v "failed" | grep ".root" | sed "s|/store/|${EOSPREFIX}/store/|" > inputFilesList_${1}_step${2}.txt && rm inputFilesList_raw_${1}_step${2}.txt
		echo "Building CRAB config file..."
		sed "s|userInputFiles = PLACEHOLDER|userInputFiles = open(\"inputFilesList_${1}_step${2}.txt\").readlines()|" mc_crabConfig_reco.py > ${CRABCONFIGFILE}
		;;
	    *)
		echo "Unrecognized second argument. Should be 1, 2, 3, or 4 for the fullsim step number. Currently: ${2}"
		exit 1
	esac
	;;
    *)
	echo "Unrecognized first argument. Should be one of \"fastsim\" or \"fullsim\". Currently: ${1}"
	exit 1
esac

cd ${CMSSWSOURCE} && eval `scramv1 runtime -sh`
echo "CMSSW_BASE: ${CMSSW_BASE}"
cd ${CFGFILESSOURCE}
source /cvmfs/cms.cern.ch/crab3/crab.sh

DRYRUNFLAG="--dryrun "
if [ "${3}" = "prod" ]; then
    DRYRUNFLAG="--wait "
fi

set -x && crab submit ${DRYRUNFLAG}-c ${CRABCONFIGFILE} ${CRABOPTIONS} && set +x
