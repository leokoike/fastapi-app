fakeTwitter = db.getSiblingDB('fakeTwitter')

fakeTwitter.createUser({
    user: 'admin',
    pwd: 'admin',
    roles: [{ role: 'readWrite', db: 'fakeTwitter' }]
});