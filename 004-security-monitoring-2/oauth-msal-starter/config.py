class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    # TODO: Enter your client secret from Azure AD below
    CLIENT_SECRET = "uzh8Q~lZy23NgadoHvt3YAMks6mY9OWSNwV_Rces" 

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    # TODO: Enter your application client ID here
    CLIENT_ID = "3e76f35c-2119-4220-9ad4-a959ee3aa793"

    # TODO: Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session