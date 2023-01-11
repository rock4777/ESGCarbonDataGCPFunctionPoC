# Registry URL for assets (not projects)
url = "https://registry.verra.org/uiapi/asset/asset/search?$skip=0&count=true&$format=csv"

# Filter for assets
data_filter = {
    "program":"VCS",
    "issuanceTypeCodes":["ISSUE"]
}

#url request header
headers = {
    "Content-Type": "application/json",
    "Host": "registry.verra.org",
    "Origin": "https://registry.verra.org",
    "Referrer": "https://registry.verra.org/app/search/vcs",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

#gcp storage bucket name
bucketName = 'esg_poc'

#esg data type
esgDType = 'carbon'