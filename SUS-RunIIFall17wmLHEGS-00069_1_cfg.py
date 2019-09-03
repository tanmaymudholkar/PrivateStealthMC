# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SUS-RunIIFall17FSPremix-00069-fragment.py --fileout file:SUS-RunIIFall17wmLHEGS-0069.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --customise_commands process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200) --step GEN,SIM --geometry DB:Extended --era Run2_2017 --python_filename SUS-RunIIFall17wmLHEGS-0069_1_cfg.py --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SUS-RunIIFall17FSPremix-00069-fragment.py nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:SUS-RunIIFall17wmLHEGS-00069.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '93X_mc2017_realistic_v3', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    RandomizedParameters = cms.VPSet(cms.PSet(
        ConfigDescription = cms.string('T5WgStealth_1000_500'),
        ConfigWeight = cms.double(170.425531915),
        GridpackPath = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/SMS-GlGl/v1/SMS-GlGl_mGl-1000_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
        PythiaParameters = cms.PSet(
            JetMatchingParameters = cms.vstring('JetMatching:setMad = off', 
                'JetMatching:scheme = 1', 
                'JetMatching:merge = on', 
                'JetMatching:jetAlgorithm = 2', 
                'JetMatching:etaJetMax = 5.', 
                'JetMatching:coneRadius = 1.', 
                'JetMatching:slowJetPower = 1', 
                'JetMatching:qCut = 140', 
                'JetMatching:nQmatch = 5', 
                'JetMatching:nJetMax = 2', 
                'JetMatching:doShowerKt = off', 
                '6:m0 = 172.5', 
                '24:mMin = 0.1', 
                'Check:abortIfVeto = on'),
            parameterSets = cms.vstring('pythia8CommonSettings', 
                'pythia8CP5Settings', 
                'JetMatchingParameters'),
            pythia8CP5Settings = cms.vstring('Tune:pp 14',
                'Tune:ee 7',
                'MultipartonInteractions:ecmPow=0.03344',
                'PDF:pSet=20',
                'MultipartonInteractions:bProfile=2',
                'MultipartonInteractions:pT0Ref=1.41',
                'MultipartonInteractions:coreRadius=0.7634',
                'MultipartonInteractions:coreFraction=0.63',
                'ColourReconnection:range=5.176',
                'SigmaTotal:zeroAXB=off',
                'SpaceShower:alphaSorder=2',
                'SpaceShower:alphaSvalue=0.118',
                'SigmaProcess:alphaSvalue=0.118',
                'SigmaProcess:alphaSorder=2',
                'MultipartonInteractions:alphaSvalue=0.118',
                'MultipartonInteractions:alphaSorder=2',
                'TimeShower:alphaSorder=2',
                'TimeShower:alphaSvalue=0.118'),
            pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
                'Main:timesAllowErrors = 10000', 
                'Check:epTolErr = 0.01', 
                'Beams:setProductionScalesFromLHEF = off', 
                'SLHA:keepSM = on', 
                'SLHA:minMassSM = 1000.', 
                'ParticleDecays:limitTau0 = on', 
                'ParticleDecays:tau0Max = 10', 
                'ParticleDecays:allowPhotonRadiation = on')
        ),
        SLHATableForPythia8 = cms.string('\nBLOCK MODSEL  # Model selection\n    1     1   sugra\n#\nBLOCK QNUMBERS 3000001 # f\n    1  0 # 3 times electric charge\n    2  2 # number of spin states (2S+1)\n    3  1 # colour rep (1: singlet, 3: triplet, 8: octet)\n    4  0 # Particle/Antiparticle distinction (0=own anti)\n#\nBLOCK QNUMBERS 3000002 # n\n    1  0 # 3 times electric charge\n    2  1 # number of spin states (2S+1)\n    3  1 # colour rep (1: singlet, 3: triplet, 8: octet)\n    4  0 # Particle/Antiparticle distinction (0=own anti)\nBLOCK MASS\n   2000001     1.00000000E+10\n   2000002     1.00000000E+10\n   2000003     1.00000000E+10\n   2000004     1.00000000E+10\n   2000005     1.00000000E+10\n   2000006     1.00000000E+10\n   2000011     1.00000000E+10\n   2000013     1.00000000E+10\n   2000015     1.00000000E+10\n   1000001     1.00000000E+10\n   1000002     1.00000000E+10\n   1000003     1.00000000E+10\n   1000004     1.00000000E+10\n   1000005     1.00000000E+10\n   1000006     1.00000000E+10\n   1000011     1.00000000E+10\n   1000012     1.00000000E+10\n   1000013     1.00000000E+10\n   1000014     1.00000000E+10\n   1000015     1.00000000E+10\n   1000016     1.00000000E+10\n   1000021     1.000000e+03\n   1000022     5.000000e+02\n   1000023     1.00000000E+10\n   1000024     5.000000e+02\n   1000025     1.00000000E+10\n   1000035     1.00000000E+10\n   1000037     1.00000000E+10\n   1000039                0.0   #  Gravitino\n   3000001     1.00000000E+02   #  f: stealth sector\n   3000002     9.00000000E+01   #  n: stealth sector\n#\nDECAY   2000001     0.00000000E+00\nDECAY   2000002     0.00000000E+00\nDECAY   2000003     0.00000000E+00\nDECAY   2000004     0.00000000E+00\nDECAY   2000005     0.00000000E+00\nDECAY   2000006     0.00000000E+00\nDECAY   2000011     0.00000000E+00\nDECAY   2000013     0.00000000E+00\nDECAY   2000015     0.00000000E+00\nDECAY   1000001     0.00000000E+00\nDECAY   1000002     0.00000000E+00\nDECAY   1000003     0.00000000E+00\nDECAY   1000004     0.00000000E+00\nDECAY   1000005     0.00000000E+00\nDECAY   1000006     0.00000000E+00\nDECAY   1000011     0.00000000E+00\nDECAY   1000012     0.00000000E+00\nDECAY   1000013     0.00000000E+00\nDECAY   1000014     0.00000000E+00\nDECAY   1000015     0.00000000E+00\nDECAY   1000016     0.00000000E+00\n\nDECAY   1000021     1.00000000E+00\n     0.00000000E+00    3         -6          6    1000022\n     1.00000000E-01    3         -1          1    1000022\n     1.00000000E-01    3         -2          2    1000022\n     1.00000000E-01    3         -3          3    1000022\n     1.00000000E-01    3         -4          4    1000022\n     1.00000000E-01    3         -5          5    1000022\n     1.25000000E-01    3         -2          1    1000024\n     1.25000000E-01    3          2         -1    -1000024\n     1.25000000E-01    3         -4          3    1000024\n     1.25000000E-01    3          4         -3    -1000024\n\nDECAY   1000022     1.00000000E-03\n     0.0000000    2     3000001        22\n     1.0000000    2     3000001        22\nDECAY   1000024     1.00000000E-03\n     0.0000000    3     3000001        -1      2\n     1.0000000    2     3000001        24\n\nDECAY   3000001   1.00000000E-06   # f decays\n     1.00000000e+00    2     1000039   3000002   # BR(f -> gs n )\nDECAY   3000002   1.00000000E-06   # n decays\n     1.00000000e+00    2          21        21   # BR(n -> g g )\n\nDECAY   1000039     0.00000000E+00\n')
    )),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


# Customisation from command line

process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
