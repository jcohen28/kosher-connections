describe("Django REST framework / React quickstart app", () => {
    const user = {
      first_name: "First",
      last_name: "Last",
      email: "some-email@gmail.com"
    };
    before(() => {
      cy.exec("npm run dev");
      cy.exec("npm run flush");
    });
    it("should be able to fill a web form", () => {
      cy.visit("/");
      cy
        .get('input[name="first_name"]')
        .type(user.first_name)
        .should("have.value", user.first_name);
    cy
        .get('input[name="last_name"]')
        .type(user.last_name)
        .should("have.value", user.last_name);
      cy
        .get('input[name="email"]')
        .type(user.email)
        .should("have.value", user.email);
      cy.get("form").submit();
    });
    // more tests here
  });
