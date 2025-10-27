# AFSEC Dashboard
## _How to Create and Register New Pages_

This guide explains how to initialize and implement new pages within the **AFSEC Dashboard**.  
The example page name used throughout is `page_name`, but you should replace it with the actual name of your page.

---

## Create the Page Folder

Create a new folder in the following directory:

`AFSEC-Archtop/AFSEC-Dashboard-Main/src/pages`

Inside that folder, create a new `.tsx` file.

---

## Add the Page Template

Open the new `.tsx` file you created and paste the following code:

```tsx
const page_name = () => {
  return (
    <Grid container spacing={{ xs: 2.5, sm: 3, lg: 3.75 }}>
      <h1>work in progress :)</h1>
    </Grid>
  );
};

export default page_name;
```

> You may also create your own component instead of using this template.

---

## Add the Page to the Routing System

Next, update the routing configuration so the page is accessible in the application.

Navigate to:

`AFSEC-Archtop/AFSEC-Dashboard-Main/src/pages`

You will update two files.

---

### 1. Update `paths.ts`

Locate the export list that contains path declarations. Add a new entry following this format:

```ts
page_name: `/${rootPaths.pagesRoot}/page_name`,
```

- Insert this below the last entry that references `rootPaths.pagesRoot`
- Replace both instances of `page_name` with your page’s name
- Save the file when done

---

### 2. Update `router.tsx`

Two modifications are required.

#### A. Add a Lazy Import

Add a constant below the existing lazy imports:

```tsx
const Page_Name = lazy(() => import('[Filepath to .tsx file]'));
```

> Ensure the component name is capitalized (React requirement).  
> Replace `[Filepath to .tsx file]` with the actual relative path.

#### B. Add the Route Configuration

Find the comment instructing where to insert new pages. Below it, add the following:

```tsx
{
  path: '/page_name',
  element: (
    <MainLayout>
      <Suspense fallback={<PageLoader />}>
        <Outlet />
      </Suspense>
    </MainLayout>
  ),
  children: [
    {
      index: true,
      element: <Page_Name />,
    },
  ],
},
```

- Replace all instances of `page_name` and `Page_Name` with your page's name

---

## You're Done

You now have a fully registered new page in the AFSEC Dashboard.  
Verify that all names match the page name you selected to avoid errors.
