import pandas as pd
import numpy as np
from numpy import genfromtxt
from statsmodels.tools import categorical
import skfuzzy as fuzz
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import ShuffleSplit
from sklearn.preprocessing import Imputer
from sklearn import datasets, cluster
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier,VotingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.cluster import KMeans
from sklearn.feature_selection import RFE
from sklearn.metrics import precision_score, recall_score, roc_auc_score,  average_precision_score, f1_score
from sklearn.cross_decomposition import PLSCanonical
from sklearn import linear_model, decomposition, datasets
from sklearn.ensemble import GradientBoostingClassifier, BaggingClassifier
from binning import bin
from sklearn.decomposition import PCA, NMF
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.naive_bayes import BernoulliNB



df=pd.read_csv("cs_new_sample.csv", sep='\t', header=0,  engine='python',keep_default_na=True,na_values='(null)',usecols=['AUDIT_DEFENSE_FLAG',	'ABANDONED_FLAG',	'FSCHA_FLAG',	'FSCHC_FLAG',	'FSCHCEZ_FLAG',	'FSCHD_FLAG',	'FSCHE_FLAG',	'FSCHF_FLAG',	'MAX_FLAG',	'MINDBENDER_FLAG',	'MISC1099_FLAG',	'NUM_CARE_CONTACTS',	'PS_FLAG',	'REFUND_TRANSFER_FLAG',	'REVENUE_FLAG',	'STATE_ATTACH_COUNT',	'STATE_REVENUE_FLAG',	'REJECTED_COUNT',	'ORDER_AMOUNT',	'ABS_ZERO_TY14',	'ABS_ZERO_TY15',	'FED_TOTAL_REFUND_AMOUNT',	'STATE_TOTAL_REFUND_AMOUNT',	'AGE_TAXPAYER',	'AGE_SPOUSE',	'DEPENDENT_LT18',	'DEPENDENT_17',	'NUM_W2',	'AGI',	'NUM_EXEMPTIONS',	'NUM_DEPENDENTS',	'AMOUNT_SALARIES_AND_WAGES',	'AMOUNT_TAXABLE_INTEREST',	'AMOUNT_TAX_EXEMPT_INTEREST',	'AMOUNT_ORDINARY_DIVIDENDS',	'AMOUNT_QUALIFIED_DIVIDENDS',	'AMOUNT_TAXABLE_OFFSETS',	'AMOUNT_ALIMONY_INCOME',	'AMOUNT_BUSINESS_INCOME',	'AMOUNT_OTHER_GAIN',	'AMOUNT_FARM_INCOME',	'AMOUNT_CAPITAL_GAIN',	'AMOUNT_IRA_DISTRIBUTIONS',	'AMOUNT_TAXABLE_IRA',	'AMOUNT_PENSIONS',	'AMOUNT_TAXABLE_PENSIONS',	'AMOUNT_SCHE',	'AMOUNT_HH_EMPLOYMENT_TAX',	'AMOUNT_UNEMPLOYMENT',	'AMOUNT_SOCIAL_SEC',	'AMOUNT_TAXABLE_SOCIAL_SEC',	'AMOUNT_OTHER_INCOME',	'AMOUNT_TOTAL_INCOME',	'AMOUNT_SELF_EMPLOYMENT_TAX',	'AMOUNT_SELF_EMPLOYMENT_RETIREMENT',	'AMOUNT_TOTAL_DEDUCTIONS',	'FLAG_ITEMIZED_DEDUCTIONS',	'AMOUNT_TAXABLE_INCOME',	'NUM_SCHC',	'BUS_NET_PROFIT',	'BUS_EXPENSE_TOTAL',	'COMPLEXITY_FLAG',	'NUM_SCHE',	'AMOUNT_DISABLED_CREDIT',	'AMOUNT_TAX_CREDITS',	'AMOUNT_RESIDENTIAL_ENERGY_CREDIT',	'AMOUNT_CHILD_CREDIT',	'AMOUNT_EDUCATION_CREDIT',	'AMOUNT_TUITION',	'AMOUNT_EDUCATOR_EXPENSE',	'AMOUNT_CERTAIN_BUSINESS_EXPENSE',	'AMOUNT_HSA',	'AMOUNT_MOVING_EXPENSE',	'AMOUNT_DEDUCTIBLE_SELF_EMPLOYMENT_TAX',	'AMOUNT_SELF_EMPLOYMENT_HEALTH_INSURANCE',	'AMOUNT_EARLY_WITHDRAWAL_PENALTY',	'AMOUNT_ALIMONY_PAID',	'AMOUNT_DOMESTIC_PRODUCTION_DEDUCTION',	'AMOUNT_ADJUSTMENTS',	'FLAG_OLD_OR_BLIND',	'FLAG_ITEMIZE_SEPARATELY',	'AMOUNT_EXEMPTIONS',	'AMOUNT_TAX',	'AMOUNT_CHILD_CARE_CREDIT',	'AMOUNT_ADDITIONAL_CHILD_CREDIT',	'AMOUNT_RETIREMENT_SAVINGS_CREDIT',	'AMOUNT_HOPE_CREDIT',	'AMOUNT_EITC',	'AMOUNT_AMT',	'AMOUNT_FOREIGN_TAX_CREDIT',	'AMOUNT_OTHER_CREDITS',	'AMOUNT_TOTAL_CREDITS',	'AMOUNT_UNREPORTED_SS_MEDICARE_TAX',	'AMOUNT_ADDITIONAL_TAX_RETIREMENT',	'AMOUNT_HOMEBUYER_CREDIT_REPAYMENT',	'AMOUNT_OTHER_TAXES',	'AMOUNT_INCOME_TAX_WITHHELD',	'AMOUNT_ESTIMATED_TAX',	'AMOUNT_NT_COMBAT_PAY',	'AMOUNT_PAID_WITH_EXTENSION',	'AMOUNT_EXCESS_SS_RRTA_WITHHELD',	'AMOUNT_FUEL_TAX_CREDIT',	'AMOUNT_OTHER_PAYMENTS',	'AMOUNT_TOTAL_PAYMENTS',	'AMOUNT_ESTIMATED_TAX_PENALTY',	'AMOUNT_INCOME_TAX',	'AMOUNT_TOTAL_TAX',	'AMOUNT_TAX_DUE',	'AMOUNT_REFUND',	'DMA_610',	'DMA_504',	'DMA_643',	'DMA_549',	'DMA_597',	'DMA_543',	'DMA_567',	'DMA_789',	'DMA_855',	'DMA_745',	'DMA_581',	'DMA_505',	'DMA_554',	'DMA_501',	'DMA_633',	'DMA_825',	'DMA_502',	'DMA_526',	'DMA_670',	'DMA_754',	'DMA_606',	'DMA_828',	'DMA_518',	'DMA_734',	'DMA_551',	'DMA_530',	'DMA_638',	'DMA_710',	'DMA_746',	'DMA_558',	'DMA_627',	'DMA_628',	'DMA_647',	'DMA_679',	'DMA_756',	'DMA_724',	'DMA_642',	'DMA_555',	'DMA_563',	'DMA_804',	'DMA_500',	'DMA_722',	'DMA_807',	'DMA_718',	'DMA_527',	'DMA_641',	'DMA_538',	'DMA_862',	'DMA_531',	'DMA_603',	'DMA_801',	'DMA_669',	'DMA_758',	'DMA_881',	'DMA_550',	'DMA_634',	'DMA_682',	'DMA_539',	'DMA_617',	'DMA_596',	'DMA_520',	'DMA_736',	'DMA_868',	'DMA_533',	'DMA_545',	'DMA_575',	'DMA_604',	'DMA_678',	'DMA_577',	'DMA_691',	'DMA_560',	'DMA_659',	'DMA_749',	'DMA_657',	'DMA_687',	'DMA_693',	'DMA_711',	'DMA_548',	'DMA_698',	'DMA_639',	'DMA_508',	'DMA_747',	'DMA_565',	'DMA_509',	'DMA_737',	'DMA_613',	'DMA_757',	'DMA_566',	'DMA_516',	'DMA_513',	'DMA_534',	'DMA_582',	'DMA_626',	'DMA_525',	'DMA_561',	'DMA_544',	'DMA_569',	'DMA_673',	'DMA_522',	'DMA_658',	'DMA_635',	'DMA_767',	'DMA_650',	'DMA_705',	'DMA_588',	'DMA_514',	'DMA_652',	'DMA_521',	'DMA_602',	'DMA_570',	'DMA_537',	'DMA_576',	'DMA_600',	'DMA_765',	'DMA_598',	'DMA_611',	'DMA_803',	'DMA_528',	'DMA_535',	'DMA_640',	'DMA_623',	'DMA_624',	'DMA_702',	'DMA_517',	'DMA_637',	'DMA_536',	'DMA_813',	'DMA_523',	'DMA_547',	'DMA_631',	'DMA_661',	'DMA_744',	'DMA_810',	'DMA_515',	'DMA_622',	'DMA_541',	'DMA_557',	'DMA_584',	'DMA_540',	'DMA_630',	'DMA_798',	'DMA_811',	'DMA_512',	'DMA_507',	'DMA_717',	'DMA_759',	'DMA_532',	'DMA_592',	'DMA_802',	'DMA_542',	'DMA_632',	'DMA_636',	'DMA_743',	'DMA_839',	'DMA_752',	'DMA_510',	'DMA_519',	'DMA_546',	'DMA_573',	'DMA_819',	'DMA_616',	'DMA_692',	'DMA_676',	'DMA_821',	'DMA_529',	'DMA_619',	'DMA_800',	'DMA_675',	'DMA_625',	'DMA_506',	'DMA_764',	'DMA_771',	'DMA_583',	'DMA_709',	'DMA_656',	'DMA_662',	'DMA_740',	'DMA_866',	'DMA_820',	'DMA_755',	'DMA_511',	'DMA_574',	'DMA_671',	'DMA_571',	'DMA_751',	'DMA_648',	'DMA_686',	'DMA_753',	'DMA_503',	'DMA_552',	'DMA_564',	'DMA_618',	'DMA_762',	'DMA_644',	'DMA_716',	'DMA_770',	'DMA_609',	'DMA_556',	'DMA_766',	'DMA_773',	'DMA_553',	'DMA_559',	'DMA_649',	'DMA_524',	'DMA_605',	'DMA_612',	'DMA_651',	'DMA_760',	'DMA_790',	'DMA_725',	'FLAG_NUM_EXEMPTIONS',	'FLAG_NUM_DEPENDENTS',	'FLAG_AMOUNT_SALARIES_AND_WAGES',	'FLAG_AMOUNT_TAXABLE_INTEREST',	'FLAG_AMOUNT_TAX_EXEMPT_INTEREST',	'FLAG_AMOUNT_ORDINARY_DIVIDENDS',	'FLAG_AMOUNT_QUALIFIED_DIVIDENDS',	'FLAG_AMOUNT_TAXABLE_OFFSETS',	'FLAG_AMOUNT_ALIMONY_INCOME',	'FLAG_AMOUNT_BUSINESS_INCOME',	'FLAG_AMOUNT_OTHER_GAIN',	'FLAG_AMOUNT_FARM_INCOME',	'FLAG_AMOUNT_CAPITAL_GAIN',	'FLAG_AMOUNT_IRA_DISTRIBUTIONS',	'FLAG_AMOUNT_TAXABLE_IRA',	'FLAG_AMOUNT_PENSIONS',	'FLAG_AMOUNT_TAXABLE_PENSIONS',	'FLAG_AMOUNT_SCHE',	'FLAG_AMOUNT_HH_EMPLOYMENT_TAX',	'FLAG_AMOUNT_UNEMPLOYMENT',	'FLAG_AMOUNT_SOCIAL_SEC',	'FLAG_AMOUNT_TAXABLE_SOCIAL_SEC',	'FLAG_AMOUNT_OTHER_INCOME',	'FLAG_AMOUNT_TOTAL_INCOME',	'FLAG_AMOUNT_SELF_EMPLOYMENT_TAX',	'FLAG_AMOUNT_SELF_EMPLOYMENT_RETIREMENT',	'FLAG_AMOUNT_TOTAL_DEDUCTIONS',	'FLAG_AMOUNT_TAXABLE_INCOME',	'FLAG_NUM_SCHC',	'FLAG_BUS_NET_PROFIT',	'FLAG_BUS_EXPENSE_TOTAL',	'FLAG_COMPLEXITY_FLAG',	'FLAG_NUM_SCHE',	'FLAG_AMOUNT_DISABLED_CREDIT',	'FLAG_AMOUNT_TAX_CREDITS',	'FLAG_AMOUNT_RESIDENTIAL_ENERGY_CREDIT',	'FLAG_AMOUNT_CHILD_CREDIT',	'FLAG_AMOUNT_EDUCATION_CREDIT',	'FLAG_AMOUNT_TUITION',	'FLAG_AMOUNT_EDUCATOR_EXPENSE',	'FLAG_AMOUNT_CERTAIN_BUSINESS_EXPENSE',	'FLAG_AMOUNT_HSA',	'FLAG_AMOUNT_MOVING_EXPENSE',	'FLAG_AMOUNT_DEDUCTIBLE_SELF_EMPLOYMENT_TAX',	'FLAG_AMOUNT_SELF_EMPLOYMENT_HEALTH_INSURANCE',	'FLAG_AMOUNT_EARLY_WITHDRAWAL_PENALTY',	'FLAG_AMOUNT_ALIMONY_PAID',	'FLAG_AMOUNT_DOMESTIC_PRODUCTION_DEDUCTION',	'FLAG_AMOUNT_ADJUSTMENTS',	'FLAG_AMOUNT_EXEMPTIONS',	'FLAG_AMOUNT_TAX',	'FLAG_AMOUNT_CHILD_CARE_CREDIT',	'FLAG_AMOUNT_ADDITIONAL_CHILD_CREDIT',	'FLAG_AMOUNT_RETIREMENT_SAVINGS_CREDIT',	'FLAG_AMOUNT_HOPE_CREDIT',	'FLAG_AMOUNT_EITC',	'FLAG_AMOUNT_AMT',	'FLAG_AMOUNT_FOREIGN_TAX_CREDIT',	'FLAG_AMOUNT_OTHER_CREDITS',	'FLAG_AMOUNT_TOTAL_CREDITS',	'FLAG_AMOUNT_UNREPORTED_SS_MEDICARE_TAX',	'FLAG_AMOUNT_ADDITIONAL_TAX_RETIREMENT',	'FLAG_AMOUNT_HOMEBUYER_CREDIT_REPAYMENT',	'FLAG_AMOUNT_OTHER_TAXES',	'FLAG_AMOUNT_INCOME_TAX_WITHHELD',	'FLAG_AMOUNT_ESTIMATED_TAX',	'FLAG_AMOUNT_NT_COMBAT_PAY',	'FLAG_AMOUNT_PAID_WITH_EXTENSION',	'FLAG_AMOUNT_EXCESS_SS_RRTA_WITHHELD',	'FLAG_AMOUNT_FUEL_TAX_CREDIT',	'FLAG_AMOUNT_OTHER_PAYMENTS',	'FLAG_AMOUNT_TOTAL_PAYMENTS',	'FLAG_AMOUNT_ESTIMATED_TAX_PENALTY',	'FLAG_AMOUNT_INCOME_TAX',	'FLAG_AMOUNT_TOTAL_TAX',	'FLAG_AMOUNT_TAX_DUE',	'FLAG_AMOUNT_REFUND',	'PRE_UPVOTES2',	'PRE_DOWNVOTES2',	'PRE_TOTAL_VOTES2',	'POST_UPVOTES2',	'POST_DOWNVOTES2',	'POST_TOTAL_VOTES2',	'NULL_OCCUPATION',	'UNEMPLOYED',	'LABOR',	'NA_OCCUPATION',	'NULL_OCCUPATION_SPOUSE'])
df.columns = df.columns.str.strip()


for column in df.columns:
    if (df[column].dtype==np.float64 or df[column].dtype==np.int64):
        df[column]=df[column].fillna(df[column].median())
    else:

        df[column] = df[column].fillna(df[column].median())


df=df.astype(float)
df_bool=df[['AUDIT_DEFENSE_FLAG',	'ABANDONED_FLAG',	'FSCHA_FLAG',	'FSCHC_FLAG',	'FSCHCEZ_FLAG',	'FSCHD_FLAG',	'FSCHE_FLAG',	'FSCHF_FLAG',	'MAX_FLAG',	'MINDBENDER_FLAG',	'MISC1099_FLAG',	'PS_FLAG',	'REFUND_TRANSFER_FLAG',	'REVENUE_FLAG',	'STATE_REVENUE_FLAG',	'ABS_ZERO_TY14',	'DEPENDENT_LT18',	'DEPENDENT_17',	'FLAG_ITEMIZED_DEDUCTIONS',	'COMPLEXITY_FLAG',	'FLAG_OLD_OR_BLIND',	'FLAG_ITEMIZE_SEPARATELY',	'DMA_610',	'DMA_504',	'DMA_643',	'DMA_549',	'DMA_597',	'DMA_543',	'DMA_567',	'DMA_789',	'DMA_855',	'DMA_745',	'DMA_581',	'DMA_505',	'DMA_554',	'DMA_501',	'DMA_633',	'DMA_825',	'DMA_502',	'DMA_526',	'DMA_670',	'DMA_754',	'DMA_606',	'DMA_828',	'DMA_518',	'DMA_734',	'DMA_551',	'DMA_530',	'DMA_638',	'DMA_710',	'DMA_746',	'DMA_558',	'DMA_627',	'DMA_628',	'DMA_647',	'DMA_679',	'DMA_756',	'DMA_724',	'DMA_642',	'DMA_555',	'DMA_563',	'DMA_804',	'DMA_500',	'DMA_722',	'DMA_807',	'DMA_718',	'DMA_527',	'DMA_641',	'DMA_538',	'DMA_862',	'DMA_531',	'DMA_603',	'DMA_801',	'DMA_669',	'DMA_758',	'DMA_881',	'DMA_550',	'DMA_634',	'DMA_682',	'DMA_539',	'DMA_617',	'DMA_596',	'DMA_520',	'DMA_736',	'DMA_868',	'DMA_533',	'DMA_545',	'DMA_575',	'DMA_604',	'DMA_678',	'DMA_577',	'DMA_691',	'DMA_560',	'DMA_659',	'DMA_749',	'DMA_657',	'DMA_687',	'DMA_693',	'DMA_711',	'DMA_548',	'DMA_698',	'DMA_639',	'DMA_508',	'DMA_747',	'DMA_565',	'DMA_509',	'DMA_737',	'DMA_613',	'DMA_757',	'DMA_566',	'DMA_516',	'DMA_513',	'DMA_534',	'DMA_582',	'DMA_626',	'DMA_525',	'DMA_561',	'DMA_544',	'DMA_569',	'DMA_673',	'DMA_522',	'DMA_658',	'DMA_635',	'DMA_767',	'DMA_650',	'DMA_705',	'DMA_588',	'DMA_514',	'DMA_652',	'DMA_521',	'DMA_602',	'DMA_570',	'DMA_537',	'DMA_576',	'DMA_600',	'DMA_765',	'DMA_598',	'DMA_611',	'DMA_803',	'DMA_528',	'DMA_535',	'DMA_640',	'DMA_623',	'DMA_624',	'DMA_702',	'DMA_517',	'DMA_637',	'DMA_536',	'DMA_813',	'DMA_523',	'DMA_547',	'DMA_631',	'DMA_661',	'DMA_744',	'DMA_810',	'DMA_515',	'DMA_622',	'DMA_541',	'DMA_557',	'DMA_584',	'DMA_540',	'DMA_630',	'DMA_798',	'DMA_811',	'DMA_512',	'DMA_507',	'DMA_717',	'DMA_759',	'DMA_532',	'DMA_592',	'DMA_802',	'DMA_542',	'DMA_632',	'DMA_636',	'DMA_743',	'DMA_839',	'DMA_752',	'DMA_510',	'DMA_519',	'DMA_546',	'DMA_573',	'DMA_819',	'DMA_616',	'DMA_692',	'DMA_676',	'DMA_821',	'DMA_529',	'DMA_619',	'DMA_800',	'DMA_675',	'DMA_625',	'DMA_506',	'DMA_764',	'DMA_771',	'DMA_583',	'DMA_709',	'DMA_656',	'DMA_662',	'DMA_740',	'DMA_866',	'DMA_820',	'DMA_755',	'DMA_511',	'DMA_574',	'DMA_671',	'DMA_571',	'DMA_751',	'DMA_648',	'DMA_686',	'DMA_753',	'DMA_503',	'DMA_552',	'DMA_564',	'DMA_618',	'DMA_762',	'DMA_644',	'DMA_716',	'DMA_770',	'DMA_609',	'DMA_556',	'DMA_766',	'DMA_773',	'DMA_553',	'DMA_559',	'DMA_649',	'DMA_524',	'DMA_605',	'DMA_612',	'DMA_651',	'DMA_760',	'DMA_790',	'DMA_725',	'FLAG_NUM_EXEMPTIONS',	'FLAG_NUM_DEPENDENTS',	'FLAG_AMOUNT_SALARIES_AND_WAGES',	'FLAG_AMOUNT_TAXABLE_INTEREST',	'FLAG_AMOUNT_TAX_EXEMPT_INTEREST',	'FLAG_AMOUNT_ORDINARY_DIVIDENDS',	'FLAG_AMOUNT_QUALIFIED_DIVIDENDS',	'FLAG_AMOUNT_TAXABLE_OFFSETS',	'FLAG_AMOUNT_ALIMONY_INCOME',	'FLAG_AMOUNT_BUSINESS_INCOME',	'FLAG_AMOUNT_OTHER_GAIN',	'FLAG_AMOUNT_FARM_INCOME',	'FLAG_AMOUNT_CAPITAL_GAIN',	'FLAG_AMOUNT_IRA_DISTRIBUTIONS',	'FLAG_AMOUNT_TAXABLE_IRA',	'FLAG_AMOUNT_PENSIONS',	'FLAG_AMOUNT_TAXABLE_PENSIONS',	'FLAG_AMOUNT_SCHE',	'FLAG_AMOUNT_HH_EMPLOYMENT_TAX',	'FLAG_AMOUNT_UNEMPLOYMENT',	'FLAG_AMOUNT_SOCIAL_SEC',	'FLAG_AMOUNT_TAXABLE_SOCIAL_SEC',	'FLAG_AMOUNT_OTHER_INCOME',	'FLAG_AMOUNT_TOTAL_INCOME',	'FLAG_AMOUNT_SELF_EMPLOYMENT_TAX',	'FLAG_AMOUNT_SELF_EMPLOYMENT_RETIREMENT',	'FLAG_AMOUNT_TOTAL_DEDUCTIONS',	'FLAG_AMOUNT_TAXABLE_INCOME',	'FLAG_NUM_SCHC',	'FLAG_BUS_NET_PROFIT',	'FLAG_BUS_EXPENSE_TOTAL',	'FLAG_COMPLEXITY_FLAG',	'FLAG_NUM_SCHE',	'FLAG_AMOUNT_DISABLED_CREDIT',	'FLAG_AMOUNT_TAX_CREDITS',	'FLAG_AMOUNT_RESIDENTIAL_ENERGY_CREDIT',	'FLAG_AMOUNT_CHILD_CREDIT',	'FLAG_AMOUNT_EDUCATION_CREDIT',	'FLAG_AMOUNT_TUITION',	'FLAG_AMOUNT_EDUCATOR_EXPENSE',	'FLAG_AMOUNT_CERTAIN_BUSINESS_EXPENSE',	'FLAG_AMOUNT_HSA',	'FLAG_AMOUNT_MOVING_EXPENSE',	'FLAG_AMOUNT_DEDUCTIBLE_SELF_EMPLOYMENT_TAX',	'FLAG_AMOUNT_SELF_EMPLOYMENT_HEALTH_INSURANCE',	'FLAG_AMOUNT_EARLY_WITHDRAWAL_PENALTY',	'FLAG_AMOUNT_ALIMONY_PAID',	'FLAG_AMOUNT_DOMESTIC_PRODUCTION_DEDUCTION',	'FLAG_AMOUNT_ADJUSTMENTS',	'FLAG_AMOUNT_EXEMPTIONS',	'FLAG_AMOUNT_TAX',	'FLAG_AMOUNT_CHILD_CARE_CREDIT',	'FLAG_AMOUNT_ADDITIONAL_CHILD_CREDIT',	'FLAG_AMOUNT_RETIREMENT_SAVINGS_CREDIT',	'FLAG_AMOUNT_HOPE_CREDIT',	'FLAG_AMOUNT_EITC',	'FLAG_AMOUNT_AMT',	'FLAG_AMOUNT_FOREIGN_TAX_CREDIT',	'FLAG_AMOUNT_OTHER_CREDITS',	'FLAG_AMOUNT_TOTAL_CREDITS',	'FLAG_AMOUNT_UNREPORTED_SS_MEDICARE_TAX',	'FLAG_AMOUNT_ADDITIONAL_TAX_RETIREMENT',	'FLAG_AMOUNT_HOMEBUYER_CREDIT_REPAYMENT',	'FLAG_AMOUNT_OTHER_TAXES',	'FLAG_AMOUNT_INCOME_TAX_WITHHELD',	'FLAG_AMOUNT_ESTIMATED_TAX',	'FLAG_AMOUNT_NT_COMBAT_PAY',	'FLAG_AMOUNT_PAID_WITH_EXTENSION',	'FLAG_AMOUNT_EXCESS_SS_RRTA_WITHHELD',	'FLAG_AMOUNT_FUEL_TAX_CREDIT',	'FLAG_AMOUNT_OTHER_PAYMENTS',	'FLAG_AMOUNT_TOTAL_PAYMENTS',	'FLAG_AMOUNT_ESTIMATED_TAX_PENALTY',	'FLAG_AMOUNT_INCOME_TAX',	'FLAG_AMOUNT_TOTAL_TAX',	'FLAG_AMOUNT_TAX_DUE',	'FLAG_AMOUNT_REFUND',	'NULL_OCCUPATION',	'UNEMPLOYED',	'LABOR',	'NA_OCCUPATION',	'NULL_OCCUPATION_SPOUSE']]
df.drop(['AUDIT_DEFENSE_FLAG',	'ABANDONED_FLAG',	'FSCHA_FLAG',	'FSCHC_FLAG',	'FSCHCEZ_FLAG',	'FSCHD_FLAG',	'FSCHE_FLAG',	'FSCHF_FLAG',	'MAX_FLAG',	'MINDBENDER_FLAG',	'MISC1099_FLAG',	'PS_FLAG',	'REFUND_TRANSFER_FLAG',	'REVENUE_FLAG',	'STATE_REVENUE_FLAG',	'ABS_ZERO_TY14',	'DEPENDENT_LT18',	'DEPENDENT_17',	'FLAG_ITEMIZED_DEDUCTIONS',	'COMPLEXITY_FLAG',	'FLAG_OLD_OR_BLIND',	'FLAG_ITEMIZE_SEPARATELY',	'DMA_610',	'DMA_504',	'DMA_643',	'DMA_549',	'DMA_597',	'DMA_543',	'DMA_567',	'DMA_789',	'DMA_855',	'DMA_745',	'DMA_581',	'DMA_505',	'DMA_554',	'DMA_501',	'DMA_633',	'DMA_825',	'DMA_502',	'DMA_526',	'DMA_670',	'DMA_754',	'DMA_606',	'DMA_828',	'DMA_518',	'DMA_734',	'DMA_551',	'DMA_530',	'DMA_638',	'DMA_710',	'DMA_746',	'DMA_558',	'DMA_627',	'DMA_628',	'DMA_647',	'DMA_679',	'DMA_756',	'DMA_724',	'DMA_642',	'DMA_555',	'DMA_563',	'DMA_804',	'DMA_500',	'DMA_722',	'DMA_807',	'DMA_718',	'DMA_527',	'DMA_641',	'DMA_538',	'DMA_862',	'DMA_531',	'DMA_603',	'DMA_801',	'DMA_669',	'DMA_758',	'DMA_881',	'DMA_550',	'DMA_634',	'DMA_682',	'DMA_539',	'DMA_617',	'DMA_596',	'DMA_520',	'DMA_736',	'DMA_868',	'DMA_533',	'DMA_545',	'DMA_575',	'DMA_604',	'DMA_678',	'DMA_577',	'DMA_691',	'DMA_560',	'DMA_659',	'DMA_749',	'DMA_657',	'DMA_687',	'DMA_693',	'DMA_711',	'DMA_548',	'DMA_698',	'DMA_639',	'DMA_508',	'DMA_747',	'DMA_565',	'DMA_509',	'DMA_737',	'DMA_613',	'DMA_757',	'DMA_566',	'DMA_516',	'DMA_513',	'DMA_534',	'DMA_582',	'DMA_626',	'DMA_525',	'DMA_561',	'DMA_544',	'DMA_569',	'DMA_673',	'DMA_522',	'DMA_658',	'DMA_635',	'DMA_767',	'DMA_650',	'DMA_705',	'DMA_588',	'DMA_514',	'DMA_652',	'DMA_521',	'DMA_602',	'DMA_570',	'DMA_537',	'DMA_576',	'DMA_600',	'DMA_765',	'DMA_598',	'DMA_611',	'DMA_803',	'DMA_528',	'DMA_535',	'DMA_640',	'DMA_623',	'DMA_624',	'DMA_702',	'DMA_517',	'DMA_637',	'DMA_536',	'DMA_813',	'DMA_523',	'DMA_547',	'DMA_631',	'DMA_661',	'DMA_744',	'DMA_810',	'DMA_515',	'DMA_622',	'DMA_541',	'DMA_557',	'DMA_584',	'DMA_540',	'DMA_630',	'DMA_798',	'DMA_811',	'DMA_512',	'DMA_507',	'DMA_717',	'DMA_759',	'DMA_532',	'DMA_592',	'DMA_802',	'DMA_542',	'DMA_632',	'DMA_636',	'DMA_743',	'DMA_839',	'DMA_752',	'DMA_510',	'DMA_519',	'DMA_546',	'DMA_573',	'DMA_819',	'DMA_616',	'DMA_692',	'DMA_676',	'DMA_821',	'DMA_529',	'DMA_619',	'DMA_800',	'DMA_675',	'DMA_625',	'DMA_506',	'DMA_764',	'DMA_771',	'DMA_583',	'DMA_709',	'DMA_656',	'DMA_662',	'DMA_740',	'DMA_866',	'DMA_820',	'DMA_755',	'DMA_511',	'DMA_574',	'DMA_671',	'DMA_571',	'DMA_751',	'DMA_648',	'DMA_686',	'DMA_753',	'DMA_503',	'DMA_552',	'DMA_564',	'DMA_618',	'DMA_762',	'DMA_644',	'DMA_716',	'DMA_770',	'DMA_609',	'DMA_556',	'DMA_766',	'DMA_773',	'DMA_553',	'DMA_559',	'DMA_649',	'DMA_524',	'DMA_605',	'DMA_612',	'DMA_651',	'DMA_760',	'DMA_790',	'DMA_725',	'FLAG_NUM_EXEMPTIONS',	'FLAG_NUM_DEPENDENTS',	'FLAG_AMOUNT_SALARIES_AND_WAGES',	'FLAG_AMOUNT_TAXABLE_INTEREST',	'FLAG_AMOUNT_TAX_EXEMPT_INTEREST',	'FLAG_AMOUNT_ORDINARY_DIVIDENDS',	'FLAG_AMOUNT_QUALIFIED_DIVIDENDS',	'FLAG_AMOUNT_TAXABLE_OFFSETS',	'FLAG_AMOUNT_ALIMONY_INCOME',	'FLAG_AMOUNT_BUSINESS_INCOME',	'FLAG_AMOUNT_OTHER_GAIN',	'FLAG_AMOUNT_FARM_INCOME',	'FLAG_AMOUNT_CAPITAL_GAIN',	'FLAG_AMOUNT_IRA_DISTRIBUTIONS',	'FLAG_AMOUNT_TAXABLE_IRA',	'FLAG_AMOUNT_PENSIONS',	'FLAG_AMOUNT_TAXABLE_PENSIONS',	'FLAG_AMOUNT_SCHE',	'FLAG_AMOUNT_HH_EMPLOYMENT_TAX',	'FLAG_AMOUNT_UNEMPLOYMENT',	'FLAG_AMOUNT_SOCIAL_SEC',	'FLAG_AMOUNT_TAXABLE_SOCIAL_SEC',	'FLAG_AMOUNT_OTHER_INCOME',	'FLAG_AMOUNT_TOTAL_INCOME',	'FLAG_AMOUNT_SELF_EMPLOYMENT_TAX',	'FLAG_AMOUNT_SELF_EMPLOYMENT_RETIREMENT',	'FLAG_AMOUNT_TOTAL_DEDUCTIONS',	'FLAG_AMOUNT_TAXABLE_INCOME',	'FLAG_NUM_SCHC',	'FLAG_BUS_NET_PROFIT',	'FLAG_BUS_EXPENSE_TOTAL',	'FLAG_COMPLEXITY_FLAG',	'FLAG_NUM_SCHE',	'FLAG_AMOUNT_DISABLED_CREDIT',	'FLAG_AMOUNT_TAX_CREDITS',	'FLAG_AMOUNT_RESIDENTIAL_ENERGY_CREDIT',	'FLAG_AMOUNT_CHILD_CREDIT',	'FLAG_AMOUNT_EDUCATION_CREDIT',	'FLAG_AMOUNT_TUITION',	'FLAG_AMOUNT_EDUCATOR_EXPENSE',	'FLAG_AMOUNT_CERTAIN_BUSINESS_EXPENSE',	'FLAG_AMOUNT_HSA',	'FLAG_AMOUNT_MOVING_EXPENSE',	'FLAG_AMOUNT_DEDUCTIBLE_SELF_EMPLOYMENT_TAX',	'FLAG_AMOUNT_SELF_EMPLOYMENT_HEALTH_INSURANCE',	'FLAG_AMOUNT_EARLY_WITHDRAWAL_PENALTY',	'FLAG_AMOUNT_ALIMONY_PAID',	'FLAG_AMOUNT_DOMESTIC_PRODUCTION_DEDUCTION',	'FLAG_AMOUNT_ADJUSTMENTS',	'FLAG_AMOUNT_EXEMPTIONS',	'FLAG_AMOUNT_TAX',	'FLAG_AMOUNT_CHILD_CARE_CREDIT',	'FLAG_AMOUNT_ADDITIONAL_CHILD_CREDIT',	'FLAG_AMOUNT_RETIREMENT_SAVINGS_CREDIT',	'FLAG_AMOUNT_HOPE_CREDIT',	'FLAG_AMOUNT_EITC',	'FLAG_AMOUNT_AMT',	'FLAG_AMOUNT_FOREIGN_TAX_CREDIT',	'FLAG_AMOUNT_OTHER_CREDITS',	'FLAG_AMOUNT_TOTAL_CREDITS',	'FLAG_AMOUNT_UNREPORTED_SS_MEDICARE_TAX',	'FLAG_AMOUNT_ADDITIONAL_TAX_RETIREMENT',	'FLAG_AMOUNT_HOMEBUYER_CREDIT_REPAYMENT',	'FLAG_AMOUNT_OTHER_TAXES',	'FLAG_AMOUNT_INCOME_TAX_WITHHELD',	'FLAG_AMOUNT_ESTIMATED_TAX',	'FLAG_AMOUNT_NT_COMBAT_PAY',	'FLAG_AMOUNT_PAID_WITH_EXTENSION',	'FLAG_AMOUNT_EXCESS_SS_RRTA_WITHHELD',	'FLAG_AMOUNT_FUEL_TAX_CREDIT',	'FLAG_AMOUNT_OTHER_PAYMENTS',	'FLAG_AMOUNT_TOTAL_PAYMENTS',	'FLAG_AMOUNT_ESTIMATED_TAX_PENALTY',	'FLAG_AMOUNT_INCOME_TAX',	'FLAG_AMOUNT_TOTAL_TAX',	'FLAG_AMOUNT_TAX_DUE',	'FLAG_AMOUNT_REFUND',	'NULL_OCCUPATION',	'UNEMPLOYED',	'LABOR',	'NA_OCCUPATION',	'NULL_OCCUPATION_SPOUSE'], axis=1, inplace=True)
# df=df.drop(('ABANDONED_FLAG','ABS_ZERO_TY14',	'ABS_ZERO_TY15',	'AUDIT_DEFENSE_FLAG',	'COMPLEXITY_FLAG',		'DEPENDENT_17',	'DEPENDENT_LT18',	'DMA_500',	'DMA_501',	'DMA_502',	'DMA_503',	'DMA_504',	'DMA_505',	'DMA_506',	'DMA_507',	'DMA_508',	'DMA_509',	'DMA_510',	'DMA_511',	'DMA_512',	'DMA_513',	'DMA_514',	'DMA_515',	'DMA_516',	'DMA_517',	'DMA_518',	'DMA_519',	'DMA_520',	'DMA_521',	'DMA_522',	'DMA_523',	'DMA_524',	'DMA_525',	'DMA_526',	'DMA_527',	'DMA_528',	'DMA_529',	'DMA_530',	'DMA_531',	'DMA_532',	'DMA_533',	'DMA_534',	'DMA_535',	'DMA_536',	'DMA_537',	'DMA_538',	'DMA_539',	'DMA_540',	'DMA_541',	'DMA_542',	'DMA_543',	'DMA_544',	'DMA_545',	'DMA_546',	'DMA_547',	'DMA_548',	'DMA_549',	'DMA_550',	'DMA_551',	'DMA_552',	'DMA_553',	'DMA_554',	'DMA_555',	'DMA_556',	'DMA_557',	'DMA_558',	'DMA_559',	'DMA_560',	'DMA_561',	'DMA_563',	'DMA_564',	'DMA_565',	'DMA_566',	'DMA_567',	'DMA_569',	'DMA_570',	'DMA_571',	'DMA_573',	'DMA_574',	'DMA_575',	'DMA_576',	'DMA_577',	'DMA_581',	'DMA_582',	'DMA_583',	'DMA_584',	'DMA_588',	'DMA_592',	'DMA_596',	'DMA_597',	'DMA_598',	'DMA_600',	'DMA_602',	'DMA_603',	'DMA_604',	'DMA_605',	'DMA_606',	'DMA_609',	'DMA_610',	'DMA_611',	'DMA_612',	'DMA_613',	'DMA_616',	'DMA_617',	'DMA_618',	'DMA_619',	'DMA_622',	'DMA_623',	'DMA_624',	'DMA_625',	'DMA_626',	'DMA_627',	'DMA_628',	'DMA_630',	'DMA_631',	'DMA_632',	'DMA_633',	'DMA_634',	'DMA_635',	'DMA_636',	'DMA_637',	'DMA_638',	'DMA_639',	'DMA_640',	'DMA_641',	'DMA_642',	'DMA_643',	'DMA_644',	'DMA_647',	'DMA_648',	'DMA_649',	'DMA_650',	'DMA_651',	'DMA_652',	'DMA_656',	'DMA_657',	'DMA_658',	'DMA_659',	'DMA_661',	'DMA_662',	'DMA_669',	'DMA_670',	'DMA_671',	'DMA_673',	'DMA_675',	'DMA_676',	'DMA_678',	'DMA_679',	'DMA_682',	'DMA_686',	'DMA_687',	'DMA_691',	'DMA_692',	'DMA_693',	'DMA_698',	'DMA_702',	'DMA_705',	'DMA_709',	'DMA_710',	'DMA_711',	'DMA_716',	'DMA_717',	'DMA_718',	'DMA_722',	'DMA_724',	'DMA_725',	'DMA_734',	'DMA_736',	'DMA_737',	'DMA_740',	'DMA_743',	'DMA_744',	'DMA_745',	'DMA_746',	'DMA_747',	'DMA_749',	'DMA_751',	'DMA_752',	'DMA_753',	'DMA_754',	'DMA_755',	'DMA_756',	'DMA_757',	'DMA_758',	'DMA_759',	'DMA_760',	'DMA_762',	'DMA_764',	'DMA_765',	'DMA_766',	'DMA_767',	'DMA_770',	'DMA_771',	'DMA_773',	'DMA_789',	'DMA_790',	'DMA_798',	'DMA_800',	'DMA_801',	'DMA_802',	'DMA_803',	'DMA_804',	'DMA_807',	'DMA_810',	'DMA_811',	'DMA_813',	'DMA_819',	'DMA_820',	'DMA_821',	'DMA_825',	'DMA_828',	'DMA_839',	'DMA_855',	'DMA_862',	'DMA_866',	'DMA_868',	'DMA_881',	'FLAG_AMOUNT_ADDITIONAL_CHILD_CREDIT',	'FLAG_AMOUNT_ADDITIONAL_TAX_RETIREMENT',	'FLAG_AMOUNT_ADJUSTMENTS',	'FLAG_AMOUNT_ALIMONY_INCOME',	'FLAG_AMOUNT_ALIMONY_PAID',	'FLAG_AMOUNT_AMT',	'FLAG_AMOUNT_BUSINESS_INCOME',	'FLAG_AMOUNT_CAPITAL_GAIN',	'FLAG_AMOUNT_CERTAIN_BUSINESS_EXPENSE',	'FLAG_AMOUNT_CHILD_CARE_CREDIT',	'FLAG_AMOUNT_CHILD_CREDIT',	'FLAG_AMOUNT_DEDUCTIBLE_SELF_EMPLOYMENT_TAX',	'FLAG_AMOUNT_DISABLED_CREDIT',	'FLAG_AMOUNT_DOMESTIC_PRODUCTION_DEDUCTION',	'FLAG_AMOUNT_EARLY_WITHDRAWAL_PENALTY',	'FLAG_AMOUNT_EDUCATION_CREDIT',	'FLAG_AMOUNT_EDUCATOR_EXPENSE',	'FLAG_AMOUNT_EITC',	'FLAG_AMOUNT_ESTIMATED_TAX',	'FLAG_AMOUNT_ESTIMATED_TAX_PENALTY',	'FLAG_AMOUNT_EXCESS_SS_RRTA_WITHHELD',	'FLAG_AMOUNT_EXEMPTIONS',	'FLAG_AMOUNT_FARM_INCOME',	'FLAG_AMOUNT_FOREIGN_TAX_CREDIT',	'FLAG_AMOUNT_FUEL_TAX_CREDIT',	'FLAG_AMOUNT_HH_EMPLOYMENT_TAX',	'FLAG_AMOUNT_HOMEBUYER_CREDIT_REPAYMENT',	'FLAG_AMOUNT_HOPE_CREDIT',	'FLAG_AMOUNT_HSA',	'FLAG_AMOUNT_INCOME_TAX',	'FLAG_AMOUNT_INCOME_TAX_WITHHELD',	'FLAG_AMOUNT_IRA_DISTRIBUTIONS',	'FLAG_AMOUNT_MOVING_EXPENSE',	'FLAG_AMOUNT_NT_COMBAT_PAY',	'FLAG_AMOUNT_ORDINARY_DIVIDENDS',	'FLAG_AMOUNT_OTHER_CREDITS',	'FLAG_AMOUNT_OTHER_GAIN',	'FLAG_AMOUNT_OTHER_INCOME',	'FLAG_AMOUNT_OTHER_PAYMENTS',	'FLAG_AMOUNT_OTHER_TAXES',	'FLAG_AMOUNT_PAID_WITH_EXTENSION',	'FLAG_AMOUNT_PENSIONS',	'FLAG_AMOUNT_QUALIFIED_DIVIDENDS',	'FLAG_AMOUNT_REFUND',	'FLAG_AMOUNT_RESIDENTIAL_ENERGY_CREDIT',	'FLAG_AMOUNT_RETIREMENT_SAVINGS_CREDIT',	'FLAG_AMOUNT_SALARIES_AND_WAGES',	'FLAG_AMOUNT_SCHE',	'FLAG_AMOUNT_SELF_EMPLOYMENT_HEALTH_INSURANCE',	'FLAG_AMOUNT_SELF_EMPLOYMENT_RETIREMENT',	'FLAG_AMOUNT_SELF_EMPLOYMENT_TAX',	'FLAG_AMOUNT_SOCIAL_SEC',	'FLAG_AMOUNT_TAX',	'FLAG_AMOUNT_TAX_CREDITS',	'FLAG_AMOUNT_TAX_DUE',	'FLAG_AMOUNT_TAX_EXEMPT_INTEREST',	'FLAG_AMOUNT_TAXABLE_INCOME',	'FLAG_AMOUNT_TAXABLE_INTEREST',	'FLAG_AMOUNT_TAXABLE_IRA',	'FLAG_AMOUNT_TAXABLE_OFFSETS',	'FLAG_AMOUNT_TAXABLE_PENSIONS',	'FLAG_AMOUNT_TAXABLE_SOCIAL_SEC',	'FLAG_AMOUNT_TOTAL_CREDITS',	'FLAG_AMOUNT_TOTAL_DEDUCTIONS',	'FLAG_AMOUNT_TOTAL_INCOME',	'FLAG_AMOUNT_TOTAL_PAYMENTS',	'FLAG_AMOUNT_TOTAL_TAX',	'FLAG_AMOUNT_TUITION',	'FLAG_AMOUNT_UNEMPLOYMENT',	'FLAG_AMOUNT_UNREPORTED_SS_MEDICARE_TAX',	'FLAG_BUS_EXPENSE_TOTAL',	'FLAG_BUS_NET_PROFIT',	'FLAG_COMPLEXITY_FLAG',	'FLAG_ITEMIZE_SEPARATELY',	'FLAG_NUM_DEPENDENTS',	'FLAG_NUM_EXEMPTIONS',	'FLAG_NUM_SCHC',	'FLAG_NUM_SCHE',	'FLAG_OLD_OR_BLIND',	'FSCHA_FLAG',	'FSCHC_FLAG',	'FSCHCEZ_FLAG',	'FSCHD_FLAG',	'FSCHE_FLAG',	'FSCHF_FLAG',	'MAX_FLAG',	'MINDBENDER_FLAG',	'MISC1099_FLAG',	'PS_FLAG',	'REFUND_TRANSFER_FLAG',	'REVENUE_FLAG',	'STATE_REVENUE_FLAG'),1)

X=df.values
X_cont=X[:,:]
# print X_cont
pca=PCA()
pca.fit(X_cont)
print (pca.explained_variance_ratio_)
print(pca.mean_)
#
# x3 = pca.transform(X_cont)
# string="pca_"
# pca_column_name=[string+`i` for i in range(x3.shape[1])]
#
#
# # print pca_column_name
# pca_df=pd.DataFrame(x3, columns=pca_column_name)
# pca_array=[]
# for i in pca_df.columns:
#     y = 'ABANDONED_FLAG'
#     df_bin = pd.concat((pca_df[i], df_bool[y]), axis=1)
#     dict=bin(df_bin,y)
#     leng=len(dict)
#     if leng>2:
#         pca_level='pcl_'
#         labels = [pca_level+ `r` for r in range(leng)]
#         pca_df[i]=pd.cut(pca_df[i], bins=leng,labels=labels, include_lowest=True)
#     elif leng<=2:
#         pca_df.drop([i], axis=1, inplace=True)
#
# pca_dummies=pd.get_dummies(pca_df)
#
#
# df_char=pd.read_csv("cs_new_sample.csv", sep='\t', header=0,  engine='python',keep_default_na=True,na_values=['(null)', 'NA'],usecols=['PAYMENT_METHOD',  	'CHANNEL',	'ENTRY_PAGE_GROUP',	'SEASON_PART',	'START_SKU',	'IMPORT_TYPE',	'FED_FORM_TYPE',	'PRODUCT_EDITION_DESCRIPTION',	'COMPLETED_SKU',	'LAST_STATUS',	'FILING_STATUS']  )
# df_char.columns = df_char.columns.str.strip()
#
#
# just_dummies=pd.get_dummies(df_char, prefix=['PAYMENT_METHOD',	'CHANNEL',	'ENTRY_PAGE_GROUP',	'SEASON_PART',	'START_SKU',	'IMPORT_TYPE',	'FED_FORM_TYPE',	'PRODUCT_EDITION_DESCRIPTION',	'COMPLETED_SKU',	'LAST_STATUS',	'FILING_STATUS'])
#
# df_trans=pd.concat([df_bool,pca_dummies,just_dummies],axis=1)
#
#
# Y=df_trans[['ABANDONED_FLAG']]
# X=df_trans.drop('ABANDONED_FLAG',1)
# response=Y.values
# dependent=X.values
# y=response[:,0]
# x=dependent[:,0:]
# print x.shape
#
# # rfecv = RFECV(estimator=DecisionTreeClassifier(max_depth=10000), step=1, cv=StratifiedKFold(2),
# #               scoring='precision')
# # x_reduced = rfecv.fit_transform(x, y)
# # print x_reduced.shape
#
# names = [
# # "Nearest Neighbors",
#          "Decision Tree",
#          "Random Forest",
#          # "AdaBoost",
#          "Neural Net",
#          "Naive Bayes",
#          "Bernouli Niave Bayes",
#          # "QDA",
#          "Bagging",
#          "ERT",
#          "GB"
#          ]
#
# classifiers = [
#     # KNeighborsClassifier(n_neighbors=50, leaf_size=1),
#     DecisionTreeClassifier(criterion='gini', max_depth=10000),
#     RandomForestClassifier(criterion='gini',n_estimators=1000, max_depth=100000, max_features='sqrt'),
#     # AdaBoostClassifier(n_estimators=1000),
#     MLPClassifier(alpha=1,activation='logistic'),
#     GaussianNB(),
#     BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True),
#     # QuadraticDiscriminantAnalysis(),
#     BaggingClassifier(n_estimators=1000, max_features=30),
#     ExtraTreesClassifier(n_estimators=1000, max_depth=10000, min_samples_split=2, random_state=0),
#     GradientBoostingClassifier(n_estimators=1000, learning_rate=1.0, max_depth=10000, random_state=0)
# ]
# #
# #
# # loop=int(((x.shape[1])**(1/2.0))*4)
# #
# # # n_components_score={}
# # # n_clusters_score={}
# # # for clust in range(x.shape[1]):
# # #     plsca = PLSCanonical(n_components=clust+10)
# # #     plsca.fit(x,y)
# # #     x2=plsca.transform(x)
# # #
# # #     X_train, X_test, y_train, y_test = train_test_split(x2, y, test_size=.3, random_state=0)
# # #     # clf=DecisionTreeClassifier(max_depth=1000)
# # #     # clf.fit(X_train, y_train)
# # #     # y_pred=clf.predict(X_test)
# # #     # f1 = f1_score(y_test, y_pred)
# # #     # n_components_score[clust + 10] = int(f1)
# # #     agglo = cluster.FeatureAgglomeration(n_clusters=clust + 10)
# # #     agglo.fit(x)
# # #     x_agglo = agglo.transform(x)
# # #     X_train, X_test, y_train, y_test = train_test_split(x_agglo, y, test_size=.3, random_state=0)
# # #     clf = RandomForestClassifier(n_estimators=200, max_depth=1000)
# # #     clf.fit(X_train, y_train)
# # #     y_pred = clf.predict(X_test)
# # #     f1 = f1_score(y_test, y_pred)
# # #     n_clusters_score[clust + 10] = int(f1)
# #
# #
# # # n_components_final= max(n_components_score.iterkeys(), key=lambda k: n_components_score[k])
# # # n_clusters_final= max(n_clusters_score.iterkeys(), key=lambda k: n_clusters_score[k])
# # # print n_clusters_final
# # #
# # # # plsca = PLSCanonical(n_components=n_components_final)
# # # # plsca.fit(x, y)
# # # # x2 = plsca.transform(x)
# # # # X_train, X_test, y_train, y_test = train_test_split(x2, y, test_size=.3, random_state=0)
# # # #
# # # # print x2.shape,x2
# # #
# # # agglo = cluster.FeatureAgglomeration(n_clusters=n_clusters_final)
# # # agglo.fit(x)
# # # x_reduced = agglo.transform(x)
# # # print x_reduced.shape
# #
# X_train, X_test, y_train, y_test =  train_test_split(x, y, test_size=.3, random_state=0)
# for name, clf in zip(names, classifiers):
#
#     clf.fit(X_train, y_train)
#     y_pred=clf.predict(X_test)
#     precision=average_precision_score(y_test, y_pred)
#     recall = recall_score(y_test, y_pred)
#     f1 = f1_score(y_test, y_pred)
#
#     print name, 'model'   , ' precision score' , precision , ' recall score', recall , ' f1 ', f1








