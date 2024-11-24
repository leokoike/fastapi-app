db.createUser({
    user: 'root',
    pwd: 'toor',
    roles: [{ role: 'readWrite', db: 'fakeTwitter' }]
});

db = db.getSiblingDB('fakeTwitter')